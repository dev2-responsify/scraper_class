from selenium import webdriver



# driver = webdriver.Chrome("/Users/responsify/Desktop/selenium_project/drivers/chromedriver")

# driver.set_page_load_timeout(10)
# driver.get("http://google.com")
# driver.refresh()


def repeat(n):
    for i in range(n):
        driver = webdriver.Chrome("/Users/responsify/Desktop/dev1/seleniumProj2/drivers/chromedriver")
        driver.set_page_load_timeout(10)
        driver.get("http://google.com")
        driver.refresh()


repeat(1)
