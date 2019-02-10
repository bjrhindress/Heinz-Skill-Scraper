# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:12:30 2019

@author: murie
"""

from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
import csv

def course_info_raw():
    html = urlopen('https://api.heinz.cmu.edu/courses_api/course_list/')
    bsyc = BeautifulSoup(html.read(), "lxml")
    # get info from all of the cells from the table of courses
    course_table = bsyc.findAll('td')
    # create a list will all course info
    course_info = []
    for c in course_table:
        for r in c:
            course_info.append(r)

    # create lists of info from the course catalog
    course_description = ["Description"]
    for x in course_info[0:317:3]:
        course_description.append(x)
        
    course_title = ["Course"]
    for x in course_info[1:317:3]:
        course_title.append(x)
     
    course_units = ["Units"]
    for x in course_info[2:317:3]:
        course_units.append(x)
    
    # create .csv file
    entries1 = [course_description, course_title, course_units]
    entries2 = zip(*entries1)
    myFile = open('cmu_raw_data.csv', 'w', newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(entries2)

course_info_raw()

def course_info_clean():
    html = urlopen('https://api.heinz.cmu.edu/courses_api/course_list/')
    bsyc = BeautifulSoup(html.read(), "lxml")
    # get info from all of the cells from the table of courses
    course_table = bsyc.findAll('td')
   
    # create a list will all course info
    course_info = []
    for c in course_table:
        for r in c:
            course_info.append(r)
            
    # create lists of info from the course catalog    
    course_title = ["Course"]
    for x in course_info[1:317:3]:
        course_title.append(x)
    
    course_units = ["Units"]
    for x in course_info[2:317:3]:
        course_units.append(x)
        
    keywords = ["Keywords", ]
    for word in course_title:
        if word in ['the', 'a','as', 'and', 'an', '&', '-', 'for']:
            pass
        else:
            key_word = [m for m in word.split()]
        keywords.extend(key_word)
    keywords = set(keywords)
    
    # creates .csv file
    entries1 = [course_title, course_units, keywords]
    entries2 = zip(*entries1)
    myFile = open('cmu_clean_data.csv', 'w', newline='')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(entries2)

if __name__ == "__main__":
	course_info_clean()