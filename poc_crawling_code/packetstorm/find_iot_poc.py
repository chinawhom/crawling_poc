##matching poc of packetstorm with iotcube cve
import re
import sys
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100): 
	formatStr = "{0:." + str(decimals) + "f}" 
	percent = formatStr.format(100 * (iteration / float(total))) 
	filledLength = int(round(barLength * iteration / float(total))) 
	bar = '#' * filledLength + '-' * (barLength - filledLength) 
	sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)), 
	if iteration == total: 
		sys.stdout.write('\n') 
		sys.stdout.flush() 

f=open('C:/Users/bibi/Desktop/lab_work/poc_processing/data/packetstorm/packetstormpoc.txt','r')
iot=open('C:/Users/bibi/Desktop/iotcube_total_cve.txt','r')
fr=open('C:/Users/bibi/Desktop/iotcube_packetstrom_poc.txt','w')
cvelist=iot.readlines()
p=re.compile('CVE-[0-9]+-[0-9]+')
datalist=f.readlines()
result=[]
for data in datalist:
	result+=p.findall(data)
result=set(result)
result=list(result)
for r in result:
	for cve in cvelist:
		if r in cve:
			fr.write(cve)
	printProgress(result.index(r),len(result),'Progress')

