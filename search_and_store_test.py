# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser

text = 'hello world'
text = urllib.parse.quote_plus(text)

url = 'https://google.com/search?q=' + text

response = requests.get(url)

#with open('output.html', 'wb') as f:
#    f.write(response.content)
#webbrowser.open('output.html')

soup = BeautifulSoup(response.text, 'lxml')
for g in soup.find_all(class_='g'):
    print(g.text)
    print('-----')


# driver = webdriver.Chrome("/Users/responsify/Desktop/selenium_project/drivers/chromedriver")

# driver.set_page_load_timeout(10)
# driver.get("http://google.com")
# driver.refresh()


# def repeat(n):
#     for i in range(n):
#         driver = webdriver.Chrome("/Users/responsify/Desktop/dev1/seleniumProj2/drivers/chromedriver")
#         driver.set_page_load_timeout(10)
#         driver.get("http://google.com")
#         #driver.refresh()
#         element_search = driver.find_element_by_name("q")
#         element_search.send_keys("Warcraft")
#         element_search.send_keys(Keys.RETURN)
  


# repeat(1)
