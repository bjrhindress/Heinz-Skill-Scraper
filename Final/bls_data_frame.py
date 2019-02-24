"""
BLS Data Access 
@author: Brian Rhindress
2/22/19

README: 

This file initializes a data frame containing employment data indexed by job titles, 
mapped to total employment, 25%, median, and 75% Annual Salary Figures 

"""

def get_job_list(df_bls):
    # all possible jobs 
    job_list = df_bls.index.values.tolist()
    
    # test with job
    sample_job = 'Financial Analysts' 
    
    	# Retrieve key indicators
    total_employment = df_bls['TOT_EMP'][sample_job]
    annual_salary_25 = df_bls['A_PCT25'][sample_job]
    annual_salary_median = df_bls['A_MEDIAN'][sample_job]
    annual_salary_75 = df_bls['A_PCT75'][sample_job]
    
    print('\nFor ', sample_job)
    print('--------------')
    print('Total Employment: ', total_employment)
    print('Annual Salary 25 Percentile: ', annual_salary_25)
    print('Annual Median Salary: ', annual_salary_median)
    print('Annual Salary 75 Percentile: ', annual_salary_75)
        
    return(job_list)

def get_df_bls():

    import pandas as pd
    import csv
    
    # read in BLS csv and set index_col = 0 to use first col (OCC_TITLE) as index
    df_bls = pd.read_csv('BLS_employment_data.csv', index_col = 0)
    
    	# Drop all non-detailed rows
    df_bls = df_bls.drop(df_bls[df_bls['OCC_GROUP']!='detailed'].index.values.tolist())
    
    # Drop all but desired Columns 
    df_bls = df_bls[['TOT_EMP','A_PCT25','A_MEDIAN','A_PCT75']]
    
    return(df_bls)
