from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bu


class LinkedinCollect():
    
    def __init__(self):
        self.seachURL=''
        self.driver=webdriver.Chrome("/Users/responsify/Desktop/dev1/seleniumProj2/drivers/chromedriver")
        self.driver.get("https://www.linkedin.com/")

    def login(self):
        # go to the login page
        logInTarget=self.driver.find_element_by_class_name('nav__button-tertiary')
        logInTarget.click()
        # go to the login
        clickJoin = self.driver.find_element_by_class_name("sign-in-link")
        clickJoin.click()
        #submit email 
        userEmail = self.driver.find_element_by_id('username')
        userEmail.send_keys('dev2@responsify.com')
        #submit password
        userPass= self.driver.find_element_by_id('password')
        userPass.send_keys('1991115ab')
        #hit submit
        loginBu= self.driver.find_element_by_class_name('login__form_action_container')
        loginBu.click()

    def search(self,name):
        search= self.driver.find_element_by_xpath('//*[@id="ember33"]/input')
        searchBYCompany="https://www.linkedin.com/search/results/companies/?keywords={}&origin=CLUSTER_EXPANSION"
        seachURL=searchBYCompany.format(name)
        self.driver=self.driver.get(searchURL)

    
        
    




collect=LinkedinCollect()
collect.login()
collect.search('Responsify')


