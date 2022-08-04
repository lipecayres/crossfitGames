###
###### Web Scrapping - Crossfit Games 2022 - Data Analysis 
###

# Prototypes
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

df1 = pd.DataFrame(championsByYear)

print(df1)
# Exporting to csv file

df1.to_csv(r'cross_recentData.csv', index = False)

