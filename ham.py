import os
import sys
reload (sys)
sys.setdefaultencoding('utf8')
import pyPdf


d={}
i=1
path="/home/ankita/Screen-Resume/allresumes/ham"

for filename in os.listdir(path):
	pdf = pyPdf.PdfFileReader(open("/home/ankita/Screen-Resume/allresumes/ham/"+filename, "rb"))
	key='h'+str(i)+".txt"
	value=filename
	d[key]=value
	f=open('h'+str(i)+".txt","w")
	a=open("allhamresumes.txt","a")
	for page in pdf.pages:
		f.write(page.extractText())
		a.write(page.extractText())
	i=i+1

print d	
