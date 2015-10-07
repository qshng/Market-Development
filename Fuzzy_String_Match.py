__author__ = 'Shuang Qiu - sqiu522@gmail.com'
#I'm matching the address from two sources - direct and mega_build using fuzzy wuzzy libraby.

from fuzzywuzzy import process
import pandas as pd
import csv

mega_build = pd.read_csv('Mega Build MDU Opps.csv')
direct = pd.read_csv('DIRECT.csv')

mega_bd_address = mega_build['Building Address']
choices = direct['Property Address 1']
result = []
dr = pd.DataFrame()

for address in mega_bd_address:
    #get match result
    top_match = process.extractOne(address, choices)
    top_match=list(top_match)
    result.append(top_match)
    #alt_match = process.extract(address, choices, limit=3)
    #get direct info
    adr = top_match[0]
    details = direct.loc[direct['Property Address 1'] == adr]
    dr=dr.append(details)

#write details to file
dr.to_csv('details.csv')

#write fuzzy-match result to file
with open('result.csv', 'wb') as csvfile:
     writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_ALL)
     for item in result:
         writer.writerow(item)

# pickle.dump(result, 'result.csv')
#pd.DataFrame.to_csv(result,'result.csv')
# print top_match, alt_match