# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:17:16 2017

@author: Alon
"""

import pandas as pd
import re

def cleanData(queries):
    good_queries=[]
    for query in queries:
        if len(query.split())>2 and len(query.split())<9 and "AND" not in query and "OR" not in query and "NOT" not in query:
            query = re.sub("[^a-zA-Z]", " ",query)
            query=re.sub(' +',' ',query)
            query=query.lstrip()
            if not query:
                continue
            good_queries.append(query)
    return good_queries

df = pd.read_csv('C:/Users/Alon/Desktop/Alon/School/4th year/project/Data files/Raw_Data1.csv', encoding="ISO-8859-1")
df['Query']=df['Query'].astype(str)
queries = df['Query']
good_queries=cleanData(queries)
new_df = pd.DataFrame()
new_df['Query']=good_queries
new_df['Result']=''
new_df['New Query']=''
new_df['Successs Rate1']=''
new_df.to_csv('C:/Users/Alon/Desktop/Alon/School/4th year/SemesterB/Data science/Project/CleanData3.csv')


df = pd.read_csv('C:/Users/Alon/Desktop/Alon/School/4th year/project/Data files/Raw_Data2.csv', encoding="ISO-8859-1")
df['Query']=df['Query'].astype(str)
queries = df['Query']
good_queries=cleanData(queries)
new_df = pd.DataFrame()
new_df['Query']=good_queries
new_df['Result']=''
new_df['New Query']=''
new_df['Successs Rate1']=''

new_df.to_csv('C:/Users/Alon/Desktop/Alon/School/4th year/SemesterB/Data science/Project/CleanData4.csv')



