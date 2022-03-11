from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from selenium.webdriver import ActionChains

links = []
game_name = []
description = []
genre = []
website = []
whitepaper = []
chain = []
community = []
marketplace = []
i = 0

with open('/root/arvin/scraper/links/l2y_selenium.csv', 'r') as file:
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


driver.get(links[0][0])
print(driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[1]/div[2]/div[3]').text)
# print(driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[1]/div[2]/div[3]/div[2]').text, type(driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[1]/div[2]/div[3]/div[2]').text))

# for link in links:
#     driver.get(link[0])
#     driver.implicitly_wait(10)
#     try:
#         genre.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[6]').text)
#     except:
#         genre.append('error')
#     try:
#         game_name.append(driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/div[1]').text)
#     except:
#         game_name.append('error')
#     try:
#         website.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[2]').text)
#     except:
#         website.append('website not found')
#     try:
#         whitepaper.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[3]').text)
#     except:
#         whitepaper.append('whitepaper not found')
#     try:
#         chain.append(driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[5]').text)
#     except:
#         chain.append('chain not found')
#     try:
#         community.append(driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[4]').text)
#     except:
#         community.append('community not found')
