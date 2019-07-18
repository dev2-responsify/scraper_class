from selenium import webdriver
form selenium import keys
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs 



# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://www.google.com/search?q=site:wikipedia.com+Black+hole&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw')
# soup = BeautifulSoup(r.text, "html.parser")
# store = soup.find_all('span')

# print(store)

    

def repeat(n):
    for i in range(n):
        driver = webdriver.Chrome("/Users/responsify/Desktop/dev1/seleniumProj2/drivers/chromedriver")
        driver.set_page_load_timeout(20)
        driver.get("https://www.linkedin.com/")
        # go to the login page
        logInTarget=driver.find_element_by_class_name('nav__button-tertiary')
        logInTarget.click()
        # go to the login
        clickJoin = driver.find_element_by_class_name("sign-in-link")
        clickJoin.click()
        #submit email 
        userEmail = driver.find_element_by_id('username')
        userEmail.send_keys('dev2@responsify.com')
        #submit password
        userPass= driver.find_element_by_id('password')
        userPass.send_keys('1991115ab')
        #hit sumit
        loginBu= driver.find_element_by_class_name('login__form_action_container')
        loginBu.click()
        
        # seach 
        search= driver.find_element_by_xpath('//*[@id="ember33"]/input')
        
        #search.send_keys(" juean marichar")
        #search.send_keys(Keys.RETURN)


    
        time.sleep(150)

       


repeat(1)
