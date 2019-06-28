from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://www.google.com/search?q=site:wikipedia.com+Black+hole&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw')
# soup = BeautifulSoup(r.text, "html.parser")
# store = soup.find_all('span')

# print(store)



def repeat(n):
    for i in range(n):
        driver = webdriver.Chrome("/Users/responsify/Desktop/dev1/seleniumProj2/drivers/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("https://www.linkedin.com/")
        #driver.refresh()
        element_search = driver.find_element_by_name("keywords")
        element_search.send_keys("Warcraft")
        element_search.send_keys(Keys.RETURN)
  


repeat(1)
