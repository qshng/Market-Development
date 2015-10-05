__author__ = 'Shuang Qiu - sqiu522@gmail.com'
#I'm matching the address from two sources - direct and mega_build using fuzzy wuzzy libraby.

from fuzzywuzzy import process
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

mega_build = pd.read_csv('Mega Build MDU Opps.csv')
direct = pd.read_csv('DIRECT.csv')

mega_bd_address = mega_build['Building Address'][:2]
choices = direct['Property Address 1']
result=[]
for address in mega_bd_address:
    top_match = process.extractOne(address, choices)
    alt_match = process.extract(address, choices, limit=3)
    adr = top_match[0]
    details = direct.loc[direct['Property Address 1'] == adr]

    print type(details) , type(top_match) , type(alt_match)

# print top_match, alt_match