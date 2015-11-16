# -*- coding: utf-8 -*-
# This program is for matching a list of address with DIRECT
import csv
from fuzzywuzzy import process
import pandas as pd

#Data Cleaning: N. -> N, convert case to proper
#read data
direct = pd.read_csv('direct1105.csv')
data = pd.read_csv('eGIS.csv')

#upper-case all DataFrame column names - place afer code for loading data aboave
#direct.columns = map(str.upper, direct.columns)
data.columns = map(str.upper, data.columns)

# bug fix for display formats to avoid run time errors - put after code for loading data above
pd.set_option('display.float_format', lambda x:'%f'%x)

mdu_id = []
match_result=[]
for address, city in zip(data['PROPERTY NAME'], data['CITY']):
#for address, city in zip(data['ADDRESS'], data['CITY']):
    #print address, city
    #Subset DIRECT by City to limit choices
    #Update: Switch from filter by Zip to by City, due to incomplete zipcode
    #choice = direct['Property Address'][direct['Property City'] == city]
    choice = direct['Property Name'][direct['Property City'] == city]
    choice = list(choice)
    #encode as unicode to avoid error
    choices = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in choice]
    #print choices

    #get match result
    top_match = process.extractOne(address, choices)

    if top_match != None:
        #get direct ID
        match = top_match[0]
        # Issue: not able to export the all columns
        #details = direct['MDU Complex ID'][direct['Property Address'] == match]
        details = direct['MDU Complex ID'][direct['Property Name'] == match]
    else:
        top_match = []
        details = []
    top_match=list(top_match)
    details=list(details)
    match_result.append(top_match)
    mdu_id.append(details)

#write details to file
with open('eGIS_details_id1.csv', 'wb') as csvfile:
     writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_ALL)
     for item in mdu_id:
         writer.writerow(item)

#write match result to file
with open('eGIS_match_result1.csv', 'wb') as csvfile:
     writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_ALL)
     for item in match_result:
         writer.writerow(item)