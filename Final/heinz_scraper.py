"""
@author: Jonathan Dyer

 NOTE
------
Must run the following commands in the appropriate conda env in order for this to work:

> conda install spacy
> python -m spacy download en
(second one must be run as admin)

Alternatively run the top command and then include the following in the code:
    import spacy
    import en_core_web_sm
    nlp = en_core_web_sm.load()
------
"""
# file: heinz_scraper.py
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
import spacy

# can replace both of these with  nlp = spacy.load('en')
# import en_core_web_sm
# nlp = en_core_web_sm.load()
nlp = spacy.load('en')


def get_course_description(link):
    # Retrieve the html
    html = urlopen(link)
    soup = BeautifulSoup(html.read(), "lxml")

    # Recover the description text (cleaned)
    text = soup.find_all('p')[2].get_text()
    clean = text.replace('\n', '').replace('\r', '')
    clean =  re.sub(r'[^\w\s]', '', clean)
    return clean;


def get_course_links():
    """
    Get a list of urls to Heinz College course description
    pages, so we can scrape each of those iteratively.

    Params
    -------
    skill_list
        A list of all the skills searched for in these pages

    Return
    -------
    <dict> {course_name: course_link, ...}
        course_name: string containing course name
        course_link: string containing link to course description page
    """
    html_base = 'https://api.heinz.cmu.edu'
    html = urlopen('https://api.heinz.cmu.edu/courses_api/course_list/')
    soup = BeautifulSoup(html.read(), "lxml")

    names = []
    links = []

    # Each course link is contained in a <tr> element with class="clickable-row"
    course_rows = soup.findAll('tr', {'class': 'clickable-row'})
    for row in course_rows:
        td = row.findAll('td')
        num = td[0].string
        name = td[1].string
        names.append(num + ": " + name)
        links.append(html_base + row.get('data-href'))

    return dict(zip(names, links))




# Main function that puts it all together
def get_skill_map(skills_list):
    """
    Returns a dict mapping each skill in the skill_list
    to a list of course names associated with that skill.
    """
    # first get the links for all Heinz courses
    course_dict = get_course_links()
    course_descriptions = course_dict.copy()

    # then scrape the description text for each link
    for name, link in course_dict.items():
        course_descriptions[name] = get_course_description(link)

#####################################################
# IF YOU CANNOT GET SPACY/NLP TO WORK:
#   Replace the next block with the following code.
#
# # we'll store the results in a new dictionary
# parsed_descriptions = course_descriptions.copy()
# for name, text in course_descriptions.items():
#     parsed_tokens = []
#
#     # remove all stopwords, punctuation, and spaces
#     for token in text.split(' '):
#         token = re.sub(r'[^\w\s]', '', token)
#         token = token.strip().lower()
#
#         if token not in ['the', 'a','as', 'and', 'an', '&', '-', 'for']:
#             parsed_tokens.append(token)
#
#     # finally add list to dictionary
#     parsed_descriptions[name] = parsed_tokens
#####################################################

    # time for a little nlp (to lemmatize the descriptions)
    # we'll store the results in a new dictionary
    parsed_descriptions = {}.fromkeys(course_descriptions.keys(), None)
    for name, text in course_descriptions.items():
        parsed_text = nlp(text)
        parsed_tokens = []

        # remove all stopwords, punctuation, and spaces
        for token in parsed_text:
            lemma = token.lemma_.lower()
            if not (nlp.vocab[lemma].is_stop or token.pos_ == 'PUNCT' or token.pos_ == 'SPACE'):
                parsed_tokens.append(lemma)

        # finally add list to dictionary
        parsed_descriptions[name] = parsed_tokens
#####################################################


    # now we can iterate through the skills list and build our final dictionary
    # give each skill its own list
    skills_to_courses = {k : [] for k in skills_list}

    for skill in skills_list:
        # now check every course for that skill
        for course_name in parsed_descriptions.keys():
            # if that skill appears in the description, add to the map
            if skill.lower() in parsed_descriptions[course_name]:
                skills_to_courses[skill].append(course_name)

    # return the final mapping
    return skills_to_courses


# write a dictionary of form {str: list} to csv
def write_to_csv(skill_map):
    with open('heinz_skills_courses.csv', 'w') as file:
        writer = csv.writer(file)
        for name, li in skill_map.items():
            entry = [name] + li
            writer.writerow(entry)

#read in the skills scraped from payscale, cleaned by the match_indeed_to_skill module
import Match_Indeed_to_skill as mi
all_skills=mi.get_skill_list()
#remove leading and trailing spaces for every skill in all skills
all_skills=[x[1:len(x)-1] for x in all_skills]

# tests if an output file called heinz_skills_courses.csv is present in the directory,
#if not, it writes the file - a full mapping of skills and heinz courses.

import pandas as pd

try: 
    pd.read_csv('heinz_skills_courses.csv')
except:
    if __name__ == '__main__':
        import sys
        
        if len(sys.argv) > 1:
            test_list = sys.argv[1:]
        else:
                
            results = get_skill_map(all_skills)
                
            write_to_csv(results)
