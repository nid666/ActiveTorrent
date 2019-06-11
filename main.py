from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import time
import re

#have user input their login details
username = input("Username:")
password = input("Password:")

#selenium used to pass login; requires firefox and geckodriver to work
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://www.torrentleech.org/user/account/login/")
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(2)


#array for the usable links that are being created using the below function
global usable_links
usable_links=[]
def get_links(index_page_number):
    index_page_prefix = "https://www.torrentleech.org/torrents/browse/index/page/"
    index_page_url = index_page_prefix+str(index_page_number)
    driver.get(index_page_url)
    soup = BeautifulSoup(driver.page_source, "lxml")

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
    #for loop that runs for the amount of torrents found on the index page
    for link in torrent_html_lines:
        #make a new string that is the actual, usable link to each torrent on the page
        usable_link = link_prefix+link_suffixes[counter]
        #print the full usable link
        #print(usable_link)
        #append the usable link to its array
        usable_links.append(usable_link)

        #add 1 to the counter to move on to the next torrent
        counter += 1

#print('PAGE 1')
get_links(1)
#print('PAGE 2')
#get_links(2)
#print('PAGE 3')
#get_links(3)

def get_torrent_info(torrent_link):
    driver.get(torrent_link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    
    #parse torrent page for number of seeders
    for seeders in soup.find_all("span", class_="seeders-text"):
        print(seeders)
        #parse the raw html string that is found for only the integer in it
        number_seeders_parsed = re.findall(r'\d+', str(seeders))
        #convert the resulting list to an integer
        number_seeders_int = int("".join(map(str, number_seeders_parsed))) 
        #print(for now) the actual integer result
        print(number_seeders_int)

    for downloads in soup.find_all(string=""):
        print(downloads)



#for x in range(0,len(usable_links)):
#    get_torrent_info(usable_links[x])

print(usable_links[0])
get_torrent_info(usable_links[0])

driver.close()
