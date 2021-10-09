import requests
import pandas as pd
from pandas.io.html import read_html
from bs4 import BeautifulSoup

""" 
page = 'https://en.wikipedia.org/wiki/List_of_Premier_League_managers'
html = requests.get(page).content
df_list = pd.read_html(html)
df = df_list[-1]
print (df[1].head())
"""

website_elements = pd.read_html('https://en.wikipedia.org/wiki/List_of_Premier_League_managers')
website = requests.get('https://en.wikipedia.org/wiki/List_of_Premier_League_managers')
website_text = BeautifulSoup(website.text, 'lxml')

tables = website_text.find_all('table', class_='wikitable')
table_coaches = tables[1]

coaches_table = website_elements[1]
coaches_table['Nationality'] = ''

for row in table_coaches.find_all('tr'):
    cells = row.find_all('td')
    print(cells)
    break

print(table_coaches)

"""     
    for cell in cells:
        country = cell.find('title=')
        print(country)

 """""" 
    if cells:
        print(cells[0].text.strip(), cells[1].text, cells[2].text)

        counter += 1
        if counter == 2:
            break
 """