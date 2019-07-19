from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bu
from urllib.request import urlopen
import time
import pickle
from random import randint



class LinkedinCollect():
    
    def __init__(self):
        
        # store info inot the scraper
        self.data=[]

         #do not overwrite 
        self.driver=webdriver.Chrome("/Users/responsify/scraper_class/searchProject/drivers/chromedriver")

        #web target 
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
        userEmail.send_keys('dev3@responsify.com')

        #submit password
        userPass= self.driver.find_element_by_id('password')
        userPass.send_keys('topsecret')

        #hit submit
        loginBu= self.driver.find_element_by_class_name('login__form_action_container')
        loginBu.click()

    def search(self,name):

        #seach advance search to the company 
        searchBYCompany="https://www.linkedin.com/search/results/companies/?keywords={}&origin=CLUSTER_EXPANSION"

        #chnage the url in Linked in
        searchURL=searchBYCompany.format(name)

        # make it too sleep 
        time.sleep(randint(10,100))
        self.driver.get(searchURL) 

        #click on the first  result
        #xpath to click on the  first company
        firstXpath="//*[contains(@class,'search-result__title t-16 t-black t-bold')]"
        value= self.driver.find_element_by_xpath(firstXpath)
        value.click()
        time.sleep(15)

        #click  on people  after  your get into company linkin
        xpathPeople="//*[contains(@data-control-name, 'topcard_see_all_employees')]"
        clickPeople=self.driver. find_element_by_xpath(xpathPeople)
        clickPeople.click()
        
       


    def scrap(self):
        
        driver=self.driver
        
        preUrl=None
        while True:
           # you need to wait before selenium updates source to the next page.
            time.sleep(randint(30,100))

            html=driver.page_source

            currectUrl=driver.current_url
            #  you have to check if you have reached the end of the page
            if preUrl==currectUrl:
                 break

            Soup=bu(html,"lxml") 
            people=Soup.findAll("div", {"class": "search-results-container"})
            self.data.append(people)
            '''#it is necessary to make sure that the page goes to the  
               #bottom before the next step'''
            driver.implicitly_wait(150)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(150)
            xpathPeople="//button[normalize-space(span) ='Next']"
            clickPeople=driver.find_element_by_xpath(xpathPeople)
            clickPeople.click()
            
            
            preUrl=currectUrl
        
         
        
        

     
    def store_agent(self):
        infoObject = []

        data = self.data

        for people in range(len(data)):

            names=data[people][0].findAll("span", {"class": "name actor-name"})
            

            tittleObj=data[people][0].findAll("p", {"class": "subline-level-1 t-14 t-black t-normal search-result__truncate"})
            
            linkedurl=data[people][0].findAll("a", {"data-control-name":"search_srp_result"})
             
            
            for i in range(len(names)):
                member={'name':None,'title':None,"url":None}

                member['title']=str(tittleObj[i].span.text)

                member['name']=str(names[i].text)

                member['url']=str(linkedurl[i*2].get('href'))

                infoObject.append([member])
        print(infoObject)

    def get_new_cookie(self):

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

         
         
        



        

        
        


        
        

    
        
    

start = time.time()
collect=LinkedinCollect()
collect.load_cookie()
collect.search('responsify')
#collect.login()
#collect.get_new_cookie()
collect.scrap()
collect.store_agent()
end = time.time()
print(end - start)