import urllib.request
from bs4 import BeautifulSoup
import re

url="https://packetstormsecurity.com/files/tags/exploit/page"
f=open('C:/Users/bibi/Desktop/packetstormpoc.txt','w')
for i in range(1663):
	html=urllib.request.urlopen(url+str(i))
	soup=BeautifulSoup(html,'html.parser')
	dllist=soup.find_all('dl')
	for dl in dllist[:-3]:
		ddlist=dl.find_all('dd')
		for dd in ddlist:
			if 'cve' == dd.get('class')[0]:
				dt=dl.find('dt')
				f.write("https://packetstormsecurity.com"+dt.find('a').get('href'))
				al=dd.find_all('a')
				for a in al:
					f.write("       "+a.text+"\n")
				break
	print("["+i"]")



