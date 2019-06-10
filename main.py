from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

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
