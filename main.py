from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import time

#selenium used to pass login; requires firefox and geckodriver to work
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://www.torrentleech.org/torrents/browse/index/page/1")
driver.find_element_by_name("username").send_keys("Samtheman801")
driver.find_element_by_name("password").send_keys("^^#XY9S1BWIoZ0ds")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "lxml")

global number
number = 0
#parse through index page and find all torrents; done by sorting for ONLY the css class="name"
for link in soup.find_all("div", class_="name"):

    #not even close to actually working, but concept is there so sam remembers
    number = number + 1
    exec("link%d = %d" % (number, number)
    print(link)

driver.close()
