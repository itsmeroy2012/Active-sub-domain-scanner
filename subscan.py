import os, sys
bspath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"BeautifulSoup4")
sys.path.append(bspath)
import ssl
from bs4 import BeautifulSoup
import urllib2,cookielib
context = ssl._create_unverified_context()
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
'''
req = urllib2.Request(site, headers=hdr)

try:
    page = BeautifulSoup(urllib2.urlopen(req,context=context).read(),'lxml')
except urllib2.HTTPError, e:
    print e.fp.read()

#content = page.read()

myTitle = page.html.head.title
'''
fn=open('subdomains.txt','r')
for word in fn.readlines():
	domain = word.strip('\r').strip('\n')
	print "[*] Scanning domain: "+str(domain)
	site = "https://"+str(domain)
	req = urllib2.Request(site, headers=hdr)
	try:
   		page = BeautifulSoup(urllib2.urlopen(req,context=context).read(),'lxml')

	except urllib2.HTTPError, e:
    		print e.fp.read()

	try:
		myTitle = page.html.head.title
		print myTitle
	except Exception, e:
		continue
		
	myTitle="Blank title"
	




