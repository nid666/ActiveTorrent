from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import time

#selenium used to pass login; requires firefox and geckodriver to work
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://www.torrentleech.org/user/account/login/")
driver.find_element_by_name("username").send_keys("Samtheman801")
driver.find_element_by_name("password").send_keys("^^#XY9S1BWIoZ0ds")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(2)



def get_links(index_page_number):
    index_page_prefix = "https://www.torrentleech.org/torrents/browse/index/page/"
    index_page_url = index_page_prefix+str(index_page_number)
    driver.get(index_page_url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    #This part is just for testing purposes to see if the cookie bypass thing worked and makes the html look better
    #print(soup.prettify())

    #defines the array for the links
    torrent_html_lines=[]
    #parse through index page and find all torrents; done by sorting for ONLY the css class="name"
    for link in soup.find_all("div", class_="name"):
        #append the raw html line (found by parsing the website) of every torrent to an array
        torrent_html_lines.append(link)

    global counter
    counter = 0
    # -------------------------------------------------------------------- #
    # THE LINK SUFFIXES ARE IN THE FOLLOWING FORMAT:                       #
    # "/torrent/[id]"                                                      #
    # THE ID IS THE NUMBER THAT THE TORRENT IS ASSIGNED BY THE WEBSITE     #
    # TO NAVIGATE TO THE TORRENT, THE FULL URL IS...                       #
    # "https://www.torrentleech.org/torrent/[id]"                          #
    # -------------------------------------------------------------------- #

    #new array to be used for the suffixes
    link_suffixes=[]
    #for loop that runs for the amount of torrents found on the index page
    for link in torrent_html_lines:
        #the characters we are looking for are chars 27-43, those are the ones that contain the suffix needed to create a full link later
        link_suffix_string = str(torrent_html_lines[counter])[27:43]
        #append the suffix to an array called link_suffixes
        link_suffixes.append(link_suffix_string)

        #add 1 to the counter to move on to the next torrent
        counter += 1

    #reset the counter to 0
    counter=0
    #what needs to be put before the suffix in order to create a proper link
    link_prefix = 'https://www.torrentleech.org'
    #array for the usable links that are being created
    usable_links=[]
    #for loop that runs for the amount of torrents found on the index page
    for link in torrent_html_lines:
        #make a new string that is the actual, usable link to each torrent on the page
        full_link = link_prefix+link_suffixes[counter]
        #print the full usable link
        print(full_link)
        #append the usable link to its array
        usable_links.append(full_link)

        #add 1 to the counter to move on to the next torrent
        counter += 1

print('PAGE 1')
get_links(1)
print('PAGE 2')
get_links(2)
print('PAGE 3')
get_links(3)

driver.close()
