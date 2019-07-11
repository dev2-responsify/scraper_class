from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bu
from urllib.request import urlopen
import time
import pickle



class LinkedinCollect():
    
    def __init__(self):
        
         #store the crapped infection
        self.company_emp=[]

        # do not overwrite 
        self.driver=webdriver.Chrome("/Users/responsify/scraper_class/searchProject/drivers/chromedriver")

        # web target 
        self.driver.get("https://www.linkedin.com/")

        #file storage for the cookie
        self.location='/Users/responsify/scraper_class/searchProject/cookies.txt'

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
        #xpath to click on the  first company
        firstXpath="//*[contains(@class,'search-result__title t-16 t-black t-bold')]"
        value= self.driver.find_element_by_xpath(firstXpath)
        value.click()
        time.sleep(10)

        #click  on people  after  your get into company linkin
        xpathPeople="(//*[contains(@class,'t-14 t-bold t-black--light org-page-navigation__item-anchor ember-view')])[3]"
        clickPeople=self.driver. find_element_by_xpath(xpathPeople)
        clickPeople.click()


    def scrap(self):

        #delete
         html=open("responsify.html", 'r')

         #correctUrl  = self.driver.current_url
         #html=self.driver.page_source

         # parse the page
         Soup=bu(html,"lxml")
         
         #get the infomaction from the people
         People_info= Soup.findAll('artdeco-entity-lockup-content')
         #value=People_info
         # store the system.
         info=self. company_emp
         size= len(People_info)

         #store the infomaction the system 
         for i in range(size):
             value=People_info[i].getText().split("\n ")
             info.append( list(filter (None,value)))
         
    def  get_new_cookie(self):

        time.sleep(20)
        location=self.location
        cookies=self.driver.get_cookie('li_at')
        #print(cookies)
        pickle.dump(cookies, open(location, "wb"))
        
    
    
    def load_cookie(self):

        cookie = pickle.load(open(self.location, "rb"))
        self.driver.delete_all_cookies()
        #selenium do not accept float values
        cookie['expiry'] = int(cookie['expiry'])
        print(cookie)
        # load the cookies
        self.driver.add_cookie(cookie)

         
         
        



        

        
        


        
        

    
        
    


collect=LinkedinCollect()



collect.load_cookie()
collect.search('responsify')
#collect.login()
#collect.get_new_cookie()


#collect.scrap()



