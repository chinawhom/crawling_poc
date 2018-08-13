import urllib.request
from bs4 import BeautifulSoup
import time
f=open('C:/Users/sskk1/Desktop/cveforgit9.txt','r')
nf=open('C:/Users/sskk1/Desktop/gitnopoclist6_google.txt','a')
gitpoc=open('C:/Users/sskk1/Desktop/gitsearchlist_google.txt',"a")
cvelist=f.readlines()
url1="https://www.google.co.kr/search?q=site%3Agithub.com+%22"
url2="%22+%22poc%22"
hdr={'User-Agent': 'Mozilla/5.0'}
find=0
num=0
for cve in cvelist:
	furl=url1+cve[:-1]+url2
	request=urllib.request.Request(furl,headers=hdr)
	response=urllib.request.urlopen(request)
	html=response.read()
	soup=BeautifulSoup(html,'html.parser')
	#print(soup)
	data=soup.find('div',{'id':'res'})
	print("["+str(num)+"]")
	#print(data)
	if '검색결과가 없습니다.' in str(soup):
		#print('[+] no result on '+cve)
		nf.write(cve)
	else:
		result=data.find('a')
		#print(soup)
		link=result.get('href')
		link=link.split('&')[0]
		link=link[7:]
		lolink=link.lower()
		if 'poc' in lolink or cve in lolink or 'exp' in lolink:
			gitpoc.write(link+"     ")
			gitpoc.write(cve)
			print("[+]"+cve)
			find+=1
	num+=1
	time.sleep(1)

print("# of find :"),
print(find)
f.close()
nf.close()
gitpoc.close()




