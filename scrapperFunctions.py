from bs4 import BeautifulSoup
import urllib

#get links from a tag and store into the list
def GetLinkFromTag(aTag, listLink):
	for a_tag in aTag:
		listLink.append(a_tag['href'])

#get links from a tag and store into a dict with text as key and link as value
def GetTextAndLinkFromTag(aTag, dictLink):
	for a_tag in aTag:
		dictLink[a_tag.text] = a_tag['href']

#get all the tags with a particular class from a link
def GetTags(link, tag, classname):
	soup = BeautifulSoup(urllib.urlopen(link),'lxml')
	# search for all the "tag" tags whose class is "classname"
	return soup.find_all(tag, class_=classname)
	#returns a COLLECTION of tags so need a for loop
	
#get links and text both and return a dict
def GetLinksAndText(link):
	divTags = GetTags(link,'div','entry-content')
	DictOfLinks={}
	for div_tag in divTags:
		#if we want to check only once than only one unordered list is to be searched
		for ul_list in div_tag.find_all('ul', limit = 1):
			GetTextAndLinkFromTag(ul_list.find_all('a'), DictOfLinks)		
	return DictOfLinks
	
#get link return a list	
def GetLinks(link, checkOnlyOnce = False):
	divTags = GetTags(link,'div','entry-content')
	listOfLinks=[]
	for div_tag in divTags:
		#find all the ordered list
		for ol_list in div_tag.find_all('ol'):
			GetLinkFromTag(ol_list.find_all('a'), listOfLinks)
		#find all the unordered list (need to find both since content can be arranged in ordered list as well as unordered list)
		for ul_list in div_tag.find_all('ul', limit = 1):
			GetLinkFromTag(ul_list.find_all('a'), listOfLinks)
				
	return listOfLinks
	
def GetLinksFromSameWebPage(link, topic):
	divTags = GetTags(link,'div','entry-content')
	listOfLinks=[]
	for div_tag in divTags:
		#find all the strong tags 
		#match the text of the strong text with our topic
		#if match then our table is the next_sibling of the parent p tag
		strongTags = div_tag.find_all('strong')
		for strong_tag in strongTags:
			if strong_tag.text.find(topic) != -1:
				for ul_tag in strong_tag.parent.find_next_siblings("ul"):
					GetLinkFromTag(ul_tag.find_all('a'), listOfLinks)
					break
				break;
	return listOfLinks
