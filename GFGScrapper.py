from bs4 import BeautifulSoup
import urllib
from generateCSV import Generate

#make a soup of the gforg website
webSiteLink = 'http://www.geeksforgeeks.org/fundamentals-of-algorithms/'
soup = BeautifulSoup(urllib.urlopen(webSiteLink),'lxml')

#find the topic list
contentlist = soup.find_all('strong')
for content in contentlist:
	if content.text.find("Topics") != -1:
		topic = content

#find all the links in the topic list
list = topic.parent.find_next_sibling()
links = list.find_all("a")

#store topic name and link in the dictionary as key and value
topicLinkDict = {}
for link in links:
	if link['href'].find('http') != -1:
		topicLinkDict[link.text] = link['href']
	else:
		topicLinkDict[link.text] = webSiteLink + link['href']
	
for key in topicLinkDict:
	Generate(key, topicLinkDict[key])
