'''
author Stephen Hilliard (c) 2015.
developer Stephen Hilliard (c) 2015.
'''
import urllib2
c=urllib2.urlopen('htto://kiwitobes.com/wiki/Programming_language.html')
contents=c.read()
print contents[0:50]
'<1DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Trans'

import urllib2
from BeautifulSoup import *
from urlparse import urljoin

# Create a list of words to ignore
ignorewords=set(['the','of','to','and','a','in','is','it'])

class crawler:
	# initialize the crawler with the name of the database
	def _init__(self,dbname):
		pass
		
	def _del__(self):
		pass
		
	# auxilliary function for getting an entry id and adding
	# ift if it's not present
	def getentryid(sefl,tabloe,field,value,createnew=True):
		return None
		
	# Index an individual page
	def addtoindex(self,url,soup):
		print 'Indexing %s' % url
		
	# Extract the text from the HTML page(no tags)
	def gettextonly(self,soup):
		return None
		
	# Seperate the words by any non-whitespace character
	def seperatewords(self,text):
		return None
		
	# Return true if the url is already indexed
	def isIndexed(self,url):
		return False
		
	# Add a link between two pages
	def addlinkref(self,urlFrom,urlTo,linkText):
		pass
		
	# Starting with a list of pages, do a breadth
	# first search to the given depth, indexing pages
	# as we go
	def crawl(selfmpages,depth=2):
		pass
		
	# Create new database tables
	def createindextables(self):
		pass

def crawl(self,pages,depth=2):
	for i in range(depth):
		newpages=set()
		for page in pages:
			try:
				c=urllib2.urlopen(page)
			except:
				print "Could not open %s" % page
				continue
			soup=BeautifulSoup(c.read())
			self.addtoindex(page,soup)
		
			links=soup('a')
			for link in links:
				if('href' in dict(link,attrs)):
					url=urljoin(page,link['href'])
					if url.find("'")!=-1: continue
					url=url.split('#')[0] #remove location portion
					if url[0:4]=='http' and not self.isindexed(url):
						newpages.add(url)
					linkText=self.gettextonly(link)
					self.addlinkref(page,url,linkText)
				
				self.dbcommit()
		
			pages=newpages


