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

df1 = pandas.merge(df_indeed, df_cmu, left_on = "Index", right_on = "Index", how = "outer")

print(df1.head(10))
print(df1)

# df2 = pandas.merge(df_cmu, df_payscale, left_on = "Index", right_on = "Index", how = "outer")
# print(df2.head(10))

#creates .csv file
with open('project_merge.csv', 'w') as myFile:
	df1.to_csv(myFile)