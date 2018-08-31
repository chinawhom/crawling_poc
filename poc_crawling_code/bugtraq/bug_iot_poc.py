import re
f=open('C:/Users/bibi/Desktop/iotcube_total_cve.txt','r')
iotlist=f.readlines()
b=open('C:/Users/bibi/Desktop/forp/bugtraq.txt','r')
buglist=b.readlines()
result=open('C:/Users/bibi/Desktop/forp/bug_iot.txt','w')
p=re.compile('CVE-[0-9]+-[0-9]+')
blist=[]

for bug in buglist:
	blist+=p.findall(bug)

blist=set(blist)
blist=list(blist)

for i in iotlist:
	if i[:-1] in blist:
		result.write(i)


