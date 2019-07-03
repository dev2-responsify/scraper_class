from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bu
from urllib.request import urlopen
import time




class LinkedinCollect():
    
    def __init__(self):
        self.seachURL=''
        # do not overwrite
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
        #seach advance search to the company 
        searchBYCompany="https://www.linkedin.com/search/results/companies/?keywords={}&origin=CLUSTER_EXPANSION"
        #chnage the url in Linked in
        searchURL=searchBYCompany.format(name)
        # make it too sleep 
        time.sleep(3)
        self.driver.get(searchURL) 
        #click on the first  result
        #xpath to lick on the  first company
        firstXpath="//*[contains(@class,'search-result__title t-16 t-black t-bold')]"
        value= self.driver.find_element_by_xpath(firstXpath)
        value.click()
         
        time.sleep(10)
        #click  on people  after  your get into company linkin
        xpathPeople="(//*[contains(@class,'t-14 t-bold t-black--light org-page-navigation__item-anchor ember-view')])[3]"
        clickPeople=self.driver. find_element_by_xpath(xpathPeople)
        clickPeople.click()


    def scrap(self):

        correctUrl  = self.driver.current_url
        html=self.driver.page_source
        soup=bu(html)
        

        
        


        
        

    
        
    


collect=LinkedinCollect()

collect.login()
collect.search('responsify')
collect.scrap()



