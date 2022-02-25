from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import pandas as pd

links = []
genre = []

with open('scraper/catherine_scraper/l2y.csv', 'r') as file:
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

for link in links[0, 10]:
    driver.get(link[0])
    driver.implicitly_wait(10)
    try:
        genre.append(driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div[2]/div[6]').text)
    except:
        genre.append('error')


genre = pd.DataFrame(genre)
genre.to_csv('genre.csv')