#!/usr/bin/env python3
# importing the libraries
from bs4 import BeautifulSoup
import requests
import os
import webbrowser
import dmenu
import sys
import wget
import datetime

#----------------------------------------------------------------------------------#
# FUNCTIONS                                                                        #
#----------------------------------------------------------------------------------#
def genList(size,start,befor,after):
	tempList=[]
	if start>0 and befor != None:
		tempList.append(str(befor))
	for x in range(size):
		tempList.append(str(x+start))
	if after != None:
		tempList.append(str(after))
	return tempList

# list of proxy "https://sites.google.com/site/freepirateproxy/"
# https://thepiratebay.rocks
entry = dmenu.show(["tv-show","movie","search"])

#all the default url should be in a conf file when i have the time...
#----------------------------------------------------------------------------------#
# SCAN                                                                             #
#----------------------------------------------------------------------------------#
if entry == "search":
	search_entry = str(dmenu.show())
	search_url = "search/"+str(search_entry)
	url_ext=search_url
elif entry == "tv-show":
	show_url = "top/205"
	url_ext=show_url
elif entry == "movie":
	 movie_url = "top/201"
	 url_ext=movie_url
tpb_url="https://thepiratebay.rocks/"
#https://thepiratebay10/
url=tpb_url+url_ext
print("URL: "+url)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

links=[]
file_name=[]
for a in soup.find_all('a', {"class": "detLink"}, href=True):
	links.append(a['href'])
	link=str(a['href']).split("/")
	file_name.append(link[5])

#a, {class="detLink"}.href
#a, target="_blank".href

