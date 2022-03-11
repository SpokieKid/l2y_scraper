import requests
from bs4 import BeautifulSoup
import csv

links = []
game_name = []
genre = []
website = []
whitepaper = []
chain = []
community = []
marketplace = []


with open('/root/arvin/scraper/links/l2y_selenium.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        links.append(row)

re = BeautifulSoup(requests.get(links[0][0]).content, 'html.parser')
re.find_all('')