from selenium import webdriver
from selenium.webdriver.common.keys import Keys



from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

#SELEIUM STUFF FOR LOGIN! ~Sam
driver = webdriver.Firefox(executable_path='geckodriver.exe')
def login():
    driver.get("https://www.torrentleech.org/user/account/login/")
    driver.find_element_by_name("username").send_keys("Samtheman801")
    driver.find_element_by_name("password").send_keys("^^#XY9S1BWIoZ0ds")
    driver.find_element_by_name("password").send_keys(Keys.ENTER)

login()


#we will have to set this part to the torrentleech html and the documentation has nothing about using cookies so we are going to have to figure out how to get our scraper past the login page
#we can navigate the different torrentleech pages with https://www.torrentleech.org/torrents/browse/index/page/ followed by the page number

website = requests.get("https://www.torrentleech.org/torrents/browse/index/page/1").text

#This will be the cookies thing to hopefull bypass the login
'''
there was stuff here but I deleted it

'''

# this part here takes website which is that whole thing and sets it to the soup and uses the lxml parser which is a super fast one

soup = BeautifulSoup(website, 'lxml')

#This part is just for testing purposes but it gets the title of the html page and sets it to title then prints it out. Helpful in making sure we are scraping the right site
title = soup.title
print(soup)
