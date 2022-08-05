###
###### Web Scrapping - Crossfit Games 2022 - Data Analysis 
###

# Prototypes
from re import I
import pandas as pd

# Site URL
url = 'https://en.wikipedia.org/wiki/CrossFit_Games'

html_cross = pd.read_html(url)

recentData = html_cross[0]
championsByYear = html_cross[1]
mastersMens = html_cross[2]
mastersWeman = html_cross[3]
teens  = html_cross[4]

# create DataFrame

# Exporting to csv file

list = []

for i in html_cross:
    df = html_cross.index(i)
    df.append(list)

print(len(list)) 

#    df1 = pd.DataFrame(df)
    
 #   name_url = "cross_{}".format(table)
    
  #  df1.to_csv(name_url + ".csv", index = False)

