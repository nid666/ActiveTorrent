from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import time
import re

#create/open file where torrent info arrays will be stored
storage_file = open("torrentinfo.txt", "a+")

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
#gets every torrent link from the index pages specified
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

    #counter used in a couple different forloops
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

#gets and stores the specified torrent's link, number of seeders, and number of downloads
def get_store_torrent_info(torrent_link):
    print('\n%s' %(torrent_link))
    driver.get(torrent_link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    
    #parse torrent page for number of downloads
    for downloads in soup.find_all("tr")[4:5]:
        #print(downloads)
        #parse the raw html string that is found for only the integer in it
        number_downloads_parsed = re.findall(r'\d+', str(downloads))
        #convert the resulting list to an integer
        number_downloads_int = int("".join(map(str, number_downloads_parsed))) 
        #print(for now) the actual integer result
        print("Downloads = %d" % number_downloads_int)

    #parse torrent page for number of seeders
    for seeders in soup.find_all("span", class_="seeders-text"):
        #print(seeders)
        #parse the raw html string that is found for only the integer in it
        number_seeders_parsed = re.findall(r'\d+', str(seeders))
        #convert the resulting list to an integer
        number_seeders_int = int("".join(map(str, number_seeders_parsed))) 
        #print(for now) the actual integer result
        print("Seeders = %d" % number_seeders_int)

    #create list of link, number of downloads, number of seeders to write to txt file
    list_to_save = [usable_links[link_array_position], str(number_downloads_int), str(number_seeders_int), '\n']

    #write the list
    with open("torrentinfo.txt", "a+") as filehandle:  
        for listitem in list_to_save:
            filehandle.write('%s ' % listitem)

#tells the program how many index pages to parse
number_index_pages_to_parse = 1
for x in range(1,(number_index_pages_to_parse+1)):
    get_links(x)

#global the position of the link that is being parsed so it can be used for both actually getting the information and for storage
#position refers to the number slot it is in in the array usable_links
global link_array_position
#get and store the needed torrent info to a txt file to be used for equations
for link_array_position in range(0,len(usable_links)):
    get_store_torrent_info(usable_links[link_array_position])

#close the selenium web page when finished
driver.close()