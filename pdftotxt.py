import os
import sys
reload (sys)
sys.setdefaultencoding('utf8')
import pyPdf


d={}
i=1
path="/home/aish/Documents/tcs/allresumes"

for filename in os.listdir(path):
	pdf = pyPdf.PdfFileReader(open("/home/aish/Documents/tcs/allresumes/"+filename, "rb"))
	key=str(i)+".txt"
	value=filename
	d[key]=value
	f=open(str(i)+".txt","w")
	for page in pdf.pages:
		f.write(page.extractText())
	i=i+1

print d	