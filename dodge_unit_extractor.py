# This program is for extract unit information from Dodge Report using regular expression

import re
import pandas as pd
import csv

dodge = pd.read_csv('Dodge 1015.csv')
feature = dodge['ADDITIONAL FEATURES']
feature = list(feature)

unit=[]

for item in feature:
    #skip nan to avoid regex error
    if isinstance(item, float):
        extract = []
    else:
        extract = re.findall('[0-9]+.(?:unit|Unit|townhome|Town|rental unit|apartment|residential'
                             '|single family|Single|total|room|dwelling|condo)',item)
    unit.append(extract)

with open('dodge.csv', 'wb') as csvfile:
     writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_ALL)
     for line in unit:
         writer.writerow(line)