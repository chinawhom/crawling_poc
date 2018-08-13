#git유형1 search코드
import urllib.request
from bs4 import BeautifulSoup
import re

url="https://github.com/Macr0phag3/Exp-or-Poc"

f=open('C:/Users/bibi/Desktop/opensisenopoclist.txt','r')
nf=open('C:/Users/bibi/Desktop/derrekrnopoclist.txt','w')
gitpoc=open('C:/Users/bibi/Desktop/derrekrpoclist.txt',"w")
cvelist=f.readlines()
pocdic={}

def makedic(a):
	global pocdic
	p=re.compile('CVE-[0-9]+-[0-9]+')
	title=p.findall(a.get('title').upper())
	for t in title:
		pocdic[t]=a.get('href')


def findpoc(url):
	request=urllib.request.urlopen(url)
	html=request.read()
	soup=BeautifulSoup(html,'html.parser')
	content=soup.find_all('td',{'class':'content'})
	print("[+]find poc on "+url)
	for c in content:
		a=c.find('a')
		if(a):
			if 'cve' in a.get('title').lower():
				makedic(a)
			else:
				if '.' not in a.get('title'):
					findpoc("https://github.com"+a.get('href'))

findpoc(url)

find=0
#for p in pocdic:
#	print(p)
for cve in cvelist:
	print("[+]"+cve)
	if cve[:-1] in pocdic:
		gitpoc.write(pocdic[cve[:-1]]+'    ')
		gitpoc.write(cve)
		find+=1
	else:
		nf.write(cve)
		a=1

print('find # : ',end="")
print(find)

f.close()
nf.close()
gitpoc.close()





#url="https://github.com/ScottyBauer/Android_Kernel_CVE_POCs"
#url="https://github.com/jiayy/android_vuln_poc-exp"
#url="https://github.com/ele7enxxh/poc-exp"
#url="https://github.com/Beep3r/POC-EXP"
#url="https://github.com/OpenSISE/CVE_PoC_Collect"
#url="https://github.com/derrekr/android_security"