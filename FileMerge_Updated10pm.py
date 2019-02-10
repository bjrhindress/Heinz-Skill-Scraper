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

df1 = pandas.merge(df_indeed, df_cmu, left_on = "Merge", right_on = "Merge", how = "inner")
df2 = pandas.merge(df1, df_payscale, left_on = "Merge", right_on = "Merge", how = "inner")

# print(df1.head(10))
# print(df1)

#creates .csv file
with open('project_merge.csv', 'w') as myFile:
	df2.to_csv(myFile)