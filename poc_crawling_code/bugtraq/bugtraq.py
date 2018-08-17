#get cve, title, date in bugtraq mail list from cve.mitre
import urllib.request
from bs4 import BeautifulSoup
import re
import time

date=''
title=''
cve=[]
mondic={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
f=open('C:/Users/sskk1/Desktop/bugtraq.txt','w')
e=open('C:/Users/sskk1/Desktop/bugtraqerrtr.txt','w')
def get_mail_info(tr):
	global date
	global title
	global cve
	tdlist=tr.find_all('td')
	td=tdlist[0]
	date=td.text[8:16]
	title=td.text[17:]
	td=tdlist[1]
	al=td.find_all('a')
	
	for a in al:
		cve.append(a.text)

def get_mail_link(url,title):
	req=urllib.request.urlopen(url)
	html=req.read()
	soup=BeautifulSoup(html,'html.parser')
	lilist=soup.find_all('li')
	for li in lilist:
		time.sleep(0.1)
		a=li.find('a')
		if a:
			if a.text == title:
				return url+"/"+a.get('href')
	return 0


url_cve="http://cve.mitre.org/data/refs/refmap/source-BUGTRAQ.html"

req=urllib.request.urlopen(url_cve)
html=req.read()
soup=BeautifulSoup(html,'html.parser')

table=soup.find_all('table')
table=table[3]
trlist=table.find_all('tr')
for mail in trlist[2:-28]:
	cve=[]
	get_mail_info(mail)
	try:
		link=get_mail_link("http://seclists.org/bugtraq/"+date[:4]+"/"+mondic[date[4:6]],title)
	except:
		e.write(title+"\n")
		continue
	if link==0:
		e.write(title+"\n")
		continue
	req=urllib.request.urlopen(link)
	html=req.read()
	soup=BeautifulSoup(html,'html.parser')
	content=soup.find('pre').text
	content=content.lower()
	if 'exploit code' in content or 'poc' in content:
		for c in cve:
			f.write(c+"        "+link+"\n")
	print("[+]"+title)


