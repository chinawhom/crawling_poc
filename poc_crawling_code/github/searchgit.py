import urllib.request
from bs4 import BeautifulSoup
import time
import sys
sys.setrecursionlimit(10000)
num=0
urlh="https://github.com/search?q="

urlt="+poc&type=Repositories"
f=open('C:/Users/sskk1/Desktop/cveforgit9.txt','r')
nf=open('C:/Users/sskk1/Desktop/gitnopoclist.txt','a')
gitpoc=open('C:/Users/sskk1/Desktop/gitsearchlist.txt',"a")
cvelist=f.readlines()
hdr = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
find=0
for cve in cvelist:
    request=urllib.request.Request(urlh+cve[:-1]+urlt, headers=hdr)
    response=urllib.request.urlopen(request)
    html=response.read()
    soup=BeautifulSoup(html,'html.parser')
    h3=soup.find_all('h3')
    print("["+str(num)+"]")
    print(h3[1])

    if not "We couldn’t find" in str(h3[1]):
        data=soup.find('div',{'class':'repo-list-item d-flex flex-column flex-md-row flex-justify-start py-4 public source'})
        result=data.find('a')
        link=result.get('href')
        link="https://github.com"+link
        gitpoc.write(link+"     ")
        gitpoc.write(cve)
        print("[+]"+cve)
        find+=1
    else:
        nf.write(cve)
    
    num+=1
    time.sleep(20)

print("# of find :"),
print(find)
f.close()
nf.close()
gitpoc.close()
