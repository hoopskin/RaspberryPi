import requests
from bs4 import BeautifulSoup

print("\n"*10000)
ignoredLinks = []
pagesVisited = []
ignoredPrefix = ["File:", "Category:", "Special:", "Wikipedia:", "Help:", "Template:", "Portal:", "Talk:", "Template_talk:"]
globalDict = {}
basePage = ""
depth = 1
maxDepth = 3
pageNumber = 1
origPage = '/wiki/Rooster_Teeth'

def isNotIgnored(link):
	for prefix in ignoredPrefix:
		if link.startswith("/wiki/"+prefix):
			return False
	#Used to remove links to a specific category. Saves time because /wiki/x and /wiki/x#letter would be different
	if link.find("#") != -1:
		return False
	return True

def getLinks(webPage):
	global pagesVisited, pageNumber

	if webPage in pagesVisited:
		return []
	else:
		pagesVisited.append(webPage)

	listLinks = []
	r = requests.get('https://en.wikipedia.org'+webPage)
	print(basePage+"\t"+webPage+"\t"+str(depth)+"\t"+str(pageNumber))
	pageNumber+=1
	#print(r.text)
	soup = BeautifulSoup(r.text, 'html.parser')
	try:
		if soup.span['class'][0] == 'mw-redirectedfrom':
			return []
	except(KeyError):
		pass
	for tag in soup.find_all('a'):
		link = tag.get('href')
		if link != None and link.startswith("/wiki/") and isNotIgnored(link):
			listLinks.append(link)

	listLinks = list(set(listLinks))
	listLinks.sort()
	return listLinks

def depthFirstSearch(webPage):
	global depth, globalDict, basePage
	#print(depth)
	rtn = getLinks(webPage)
	for page in rtn:
		if webPage == origPage:
			basePage = page
		if page in pagesVisited:
			continue
		globalDict[webPage] = rtn
		if depth == maxDepth:
			break
		depth+=1
		depthFirstSearch(page)
	depth-=1
	#print(depth)

def breadthFirstSearch(pageList):
	global depth, globalDict
	nextLevelList = []
	pageList = list(set(pageList)-set(pagesVisited))
	pageList.sort()
	for page in pageList:
		links = getLinks(page)
		globalDict[page] = links
		nextLevelList.extend(links)
	depth+=1
	breadthFirstSearch(nextLevelList)


try:
	#depthFirstSearch(origPage)
	breadthFirstSearch([origPage])
except(KeyboardInterrupt):
	pass
except(Exception):
	pass

#This produces an 8.5MB file / 1000 pages (vs. 8MB for the other file)
#with open("strOutput.txt", "wt") as f:
#	f.write(str(globalDict))
with open("listOutput.txt", "wt") as f:
	for key in list(globalDict.keys()):
		f.write(key+"\n")
		for val in globalDict[key]:
			f.write("-"+val+"\n")
print(globalDict)
print(globalDict.keys())