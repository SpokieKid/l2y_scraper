from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.headless = True

display = Display(visible=0, size=(800,600))
display.start()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

links = pd.read_csv('scraper/catherine_scraper/l2y.csv')
genre = []

for link in links:
    driver.get(link)
    driver.implicitly_wait(10)
    genre.append(driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/div[2]/div[6]/span[2]').text)


genre = pd.DataFrame(genre)
pd.DataFrame.to_csv(genre)