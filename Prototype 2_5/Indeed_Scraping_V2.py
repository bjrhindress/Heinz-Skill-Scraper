# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:38:49 2019

@author: murie
"""

#define function that scrapes one page at a time and returns a panda dataframe
def scrape_page(page_num):
    import requests  # b_soup_1.py
    import re
    from bs4 import BeautifulSoup
    #spoof the user agent to make page scrapable
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#define position search term (one word) and location
    position='analyst'
    location='Pittsburgh,+PA'
    page_str=str(page_num)
#url for search query
    url='https://www.indeed.com/jobs?q='+position+'&l='+location+'&start='+page_str
    search_page=requests.get(url,headers=headers)
    search_page
    soup=BeautifulSoup(search_page.content,'html.parser')
    all_cards=soup.find_all(class_='jobsearch-SerpJobCard row result')
#empty list to store job posting urls
    job_urls=[]
#it seems to be easier to pull posting dates and locations from search page, so do that here
    posting_dates=[]
    locations=[]
#iterate through all_cards, extract job posting urls, posting dates, and locations
    for card in all_cards:
    #urls
        job_id=card['data-jk']
        job_url='https://www.indeed.com/viewjob?jk='+job_id
        job_urls.append(job_url)
    #posting dates
    #some jobs don't have posting dates so try them
        try:
            job_post_date=card.find(class_='date').get_text()
        except:
            job_post_date=' '
        posting_dates.append(job_post_date)
    #locations
        job_location=card.find(class_='location').get_text()
        locations.append(job_location)
#locations
#lets make this dataframe
#declare the empty lists that will become columns
    position_name=[]
    employer=[]
    full_description=[]
#in the future, we can develop a list of keywords that we'll 
  #search postings for, but for now, just return all capitalized
   #words besides common words
    capital_words=[]
    for job_url in job_urls:
    #retrieve job page
        job_page=requests.get(job_url,headers=headers)
    #make job page into BeautifulSoup object
        job_soup=BeautifulSoup(job_page.content,'html.parser')
    #retrieve the job title
        job_position=job_soup.find(class_='icl-u-xs-mb--xs').get_text()
    #retrieve company name from job rating line on page
        job_rating_line=job_soup.find(class_='jobsearch-InlineCompanyRating')
        job_employer=job_rating_line.find(class_='icl-u-lg-mr--sm').get_text()
    #retrieve full job description
        job_descrip=job_soup.find(class_='jobsearch-JobComponent-description').get_text()
    #replace line breaks in description with spaces
        job_descrip.replace('\n',' ')
    #find capitalized words in job description
    
        capitals=re.findall('([A-Z][a-z]+)', job_descrip)
    #replace commonly capitalized words
        for x in ['The','Our','A','As','On','Using','We', 'In', 'Some']:
            try:
                capitals[:]=(value for value in capitals if value!=x)
            except:
                capitals
    #make capitals into a set instead of a list
        capitals=set(capitals)
    #append all of the items created to the empty lists from last step
        position_name.append(job_position)
        employer.append(job_employer)
        full_description.append(job_descrip)
        capital_words.append(capitals)
#store results in dictionary, then data frame
    import pandas as pd
    result_dict={'Job Title':position_name,
                'Employer':employer,
                'Location':locations,
                'Posting Date':posting_dates, 
                'Posting Url':job_urls,
                'Full Job Description':full_description,
                }
    result_frame=pd.DataFrame(result_dict)
    result_frame.to_csv(r'indeed_raw_data.csv')

#store results in dictionary, then data frame
    import pandas as pd
    result_dict={'Job Title':position_name,
                'Employer':employer,
                'Location':locations,
                'Posting Date':posting_dates, 
                'Posting Url':job_urls,
                'Full Job Description':full_description,
                'Keywords':capital_words
                }
    result_frame=pd.DataFrame(result_dict)
    result_frame.to_csv(r'indeed_clean_data.csv')

scrape_page(0)

