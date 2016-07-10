from generateCSV import Generate
from scrapperFunctions import GetLinksAndText

#make a soup of the gforg website
webSiteLink = 'http://www.geeksforgeeks.org/fundamentals-of-algorithms/'

#store topic name and link in the dictionary as key and value
topicLinkDict = GetLinksAndText(webSiteLink)
for key in topicLinkDict:
	if topicLinkDict[key].find('http') == -1:
		topicLinkDict[key] = webSiteLink + topicLinkDict[key]

for key in topicLinkDict:
	Generate(key, topicLinkDict[key])
