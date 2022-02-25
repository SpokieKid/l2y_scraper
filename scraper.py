from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import pandas as pd

links = []
genre = []
website = []
whitepaper = []
chain = []
community = []
marketplace = []
i = 0

with open('/root/arvin/scraper/catherine_scraper/l2y.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        links.append(row)


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.headless = True

display = Display(visible=0, size=(800,600))
display.start()
driver = webdriver.Chrome('/root/.wdm/drivers/chromedriver/linux64/98.0.4758.80/chromedriver',options=options)


for link in links:
    driver.get(link[0])
    driver.implicitly_wait(10)
    try:
        genre.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[6]').text)
    except:
        genre.append('error')
    try:
        website.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[2]').text)
    except:
        website.append('website not found')
    try:
        whitepaper.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[3]').text)
    except:
        whitepaper.append('whitepaper not found')
    try:
        chain.append(driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[5]').text)
    except:
        chain.append('chain not found')
    try:
        community.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[4]').text)
    except:
        community.append('community not found')
    
    
    

final = pd.DataFrame(genre,whitepaper,community,website,chain)
final.to_csv('/root/arvin/scraper/catherine_scraper/genre_3.csv')