import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'https://l2y.com/projects/cryptobrewmaster'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
# spans = soup.find_all('span')
# print(spans)