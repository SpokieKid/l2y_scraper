import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

links = []
genre = []
i = 0

with open('/root/arvin/scraper/catherine_scraper/l2y.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        links.append(row)

for link in links:
    try:
        url = link[0]
    except:
        url = link[0]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    spans = soup.find_all('span', {'class' : 'item'})
    lines = [span.get_text() for span in spans]
    for line in lines:
        if line == 'Genre':
            genre.append(lines[i+1])
        i += 1

genre = pd.DataFrame(genre)
genre.to_csv('/root/arvin/scraper/catherine_scraper/genre.csv')
