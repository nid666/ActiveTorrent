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
driver.find_element_by_name("username").send_keys("Samtheman801")
driver.find_element_by_name("password").send_keys("^^#XY9S1BWIoZ0ds")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "lxml")
#This part is just for testing purposes to see if the cookie bypass thing worked and makes the html look better
#print(soup.prettify())

#defines the array for the links
links=[]
#parse through index page and find all torrents; done by sorting for ONLY the css class="name"
for link in soup.find_all("div", class_="name"):
    links.append(link)

global number
number = 0
#defines a new array for the cleaned up links
fixed_links=[]
#this will go through the whole array and print every link followed by appending the fixed links to fixed_links array
for link in links:
    num_link = links[number]
    print(num_link)
    #the next line is the only one with errors, beginning of the stuff we want is at character 27. It only keeps the first through 5th character in the string
    num_link.values[1:5]
    #next line increases var number by 1 to set num_link to the next url in the links array
    number = number + 1
driver.close()
