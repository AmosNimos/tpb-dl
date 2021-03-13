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

# list of proxy "https://sites.google.com/site/freepirateproxy/"
##Select a category
url_ext=""
entry = dmenu.show(["tv-show","movie","search"], prompt='Page:')
if entry == "search":
	search_entry = str(dmenu.show([], prompt='Search:'))
	search_url = "search/"+str(search_entry)
	url_ext=search_url
elif entry == "tv-show":
	show_url = "top/205"
	url_ext=show_url
elif entry == "movie":
	 movie_url = "top/201"
	 url_ext=movie_url

##Extract available files from site 
tpb_url="https://thepiratebay.rocks/"
url=tpb_url+url_ext
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

##Store files link and titles in list 
links=[]
file_name=[]
for results in soup.find_all('a', {"class": "detLink"}, href=True):
	links.append(results['href'])
	link=str(results['href']).split("/")
	file_name.append(link[5])

entry = dmenu.show(file_name, prompt='File:')
number=0
result=""
for index in links:
	if entry in index:
		result=number
	number+=1
url=links[result]
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
links=[]
file_name=[]
for results in soup.find_all('a', href=True):
	if "magnet:" in results['href']:
		magnet_link=results['href']
webbrowser.open(str(magnet_link))
