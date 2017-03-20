import os, json, sys
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
pin='680004'
str1=""
li=[]
#print type(li)
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"}
response = requests.get('http://www.ifsccodechk.com/'+pin, headers=header)
#print(response)
soup = BeautifulSoup(response.text, 'lxml')
for script in soup(["script", "style"]):
    script.extract() 
raw=soup.getText()
#raw=raw.replace('\n',' ')

#raw=raw.split("")
raw=TextBlob(raw)
#raw=unicode(str(raw.encode('utf-8'))
raw.sentences
for i in raw.sentences:
	li.append(str(i))
	#print str(i)
	str1=str1+str(i)+"\n"
	
q=open("s1.txt","w")
q.write(str1)
for i in li:
	print(i)
	print ('\n\n')
#print li
#print(soup.getText())