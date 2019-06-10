from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait 
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import time

#selenium used to pass login; requires firefox and geckodriver to work
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://www.torrentleech.org/torrents/browse/index/page/1")
driver.find_element_by_name("username").send_keys("")
driver.find_element_by_name("password").send_keys("")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "lxml")
#This part is just for testing purposes to see if the cookie bypass thing worked and makes the html look better
#print(soup.prettify())

number = 0
#parse through index page and find all torrents; done by sorting for ONLY the css class="name"
for link in soup.find_all("div", class_="name"):
    number = (number + 1)
    print(link)
    

    basename = 'link'
    numberid = str(number)
    fullna


driver.close()
