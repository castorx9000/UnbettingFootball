import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser

import requests
import pandas as pd
from pandas.io.html import read_html
from bs4 import BeautifulSoup

def url_get_contents(url):
    
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    return f.read()

matches = pd.read_csv('Football_MetriX\df_Euro_Leagues_coaches_utf-8.csv')
print(matches.head(5))

xhtml = url_get_contents('https://en.wikipedia.org/wiki/2000%E2%80%9301_FA_Premier_League').decode('utf-8')
p = HTMLTableParser()
p.feed(xhtml)
#pprint(p.tables[3])

table_personnel_and_kits = pd.DataFrame(p.tables[3])
print(table_personnel_and_kits)