###
###### Web Scrapping - Crossfit Games 2022 - Data Analysis 
###

# Prototypes
import pandas as pd

# Site URL
url = 'https://en.wikipedia.org/wiki/CrossFit_Games'

# list of scrapped tables

html_cross = pd.read_html(url)

# Getting each table

recentData = html_cross[0]
championsByYear = html_cross[1]
mastersMens = html_cross[2]
mastersWeman = html_cross[3]
teens  = html_cross[4]

    # Create and export do csv - DataFrame 1

df1 = pd.DataFrame(recentData)
df1.to_csv(r'recentData.csv', index = False)

    # Create and export do csv - DataFrame 1

df2 = pd.DataFrame(championsByYear)
df2.to_csv(r'championsByYear.csv', index = False)

    # Create and export do csv - DataFrame 1

df3 = pd.DataFrame(mastersMens)
df3.to_csv(r'mastersMens.csv', index = False)

    # Create and export do csv - DataFrame 1

df4 = pd.DataFrame(mastersWeman)
df4.to_csv(r'mastersWeman.csv', index = False)

    # Create and export do csv - DataFrame 1

df1 = pd.DataFrame(teens)
df1.to_csv(r'teens.csv', index = False)
