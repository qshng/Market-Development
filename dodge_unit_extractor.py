__author__ = 'ading001c'
import re
hand = open('.csv')
for line in hand:
    line = line.rstrip()
    if re.search('^unit',line): #search for line start with unit, same as line.startswith
        print line
x = ["Four 10-story towers - five 11-story residential towers around Lake Peterson - two 9-story hotel towers facing Devon Avenue & four levels of retail below the hotels",
     "48 unit residential housing development with three identical 2-story, 16 unit buildings - mix of 1 bedroom (12 units), 2 bedroom (24 units) and 3 bedroom (12 units) apartments - units range in size from 680 to 1,125 square feet",
     "Interior upgrades to 534 unit apartment complex including kitchen replacement - community room - two playgrounds - replacing pool with splash pad & upgrading doors - entrances & siding",
     "801 residential properties that include row homes, town homes, condos, single-family housing, apartments, and senior rental units",
     "4-unit townhouse building (6,528 square feet of living space & 2,755 square feet of unheated garage)"]
unit=[]
a = ['unit','apartment','residential','bed']
for item in x:
    extract = re.findall('([0-9]+).(?:unit|rental unit|apartment|residential|single family)',item)
    #extract = re.findall('\d+(?:\.\d+)?[\s-]\w+',item)

    unit.append(extract)
print unit
# Wild card character -