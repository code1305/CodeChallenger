from bs4 import BeautifulSoup
import urllib
import re

def GetLinkFromTag(aTag, listLink):
	for a_tag in aTag:
		listLink.append(a_tag['href'])
	
def GetLinks(link):
	soup = BeautifulSoup(urllib.urlopen(link),'lxml')
	# search for all the "div" tags whose class is "entry-content"
	divTags = soup.find_all('div', class_='entry-content')
	#returns a COLLECTION of tags so need a for loop
	listOfLinks=[]
	for div_tag in divTags:
		#find all the ordered list
		for ol_list in div_tag.find_all('ol'):
			GetLinkFromTag(ol_list.find_all('a'), listOfLinks)
		#find all the unordered list (need to find both since content can be arranged in ordered list as well as unordered list)
		for ul_list in div_tag.find_all('ul'):
			GetLinkFromTag(ul_list.find_all('a'), listOfLinks)
	return listOfLinks

def DumpToFile(list, topic):
	writeHandle = open(str(topic)+'.txt', 'w');
	for link in list:
		print >> writeHandle, link 
	
	
def Generate(topic, link):
	listLinks = GetLinks(link)
	DumpToFile(listLinks, topic)
