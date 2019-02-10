# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:57:01 2019

@author: murie
"""

import pandas
import csv

df_cmu = pandas.read_csv('cmu_clean_data.csv')
df_payscale = pandas.read_csv('payscale_clean_data.csv')
df_indeed = pandas.read_csv('indeed_clean_data.csv')

df1 = pandas.merge(df_indeed, df_payscale, left_on = "Keywords", right_on = "PopularSkills", how = "outer")

print(df1.head(10))


df2 = pandas.merge(df_cmu, df_payscale, left_on = "Course", right_on = "PopularSkills", how = "outer")
print(df2.head(10))

# creates .csv file
myFile = open('project_merge.csv', 'w', newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(df2)