import os, json, sys
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
def getpin(pin,bank):
	#pin='680001'
	str1="Could not find any branches of "+bank+ "in your locality"
	li=[]
	#print type(li)
	header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"}
	response = requests.get('http://www.ifsccodechk.com/'+pin, headers=header)
	#print(response)
	soup = BeautifulSoup(response.text, 'lxml')
	#print(soup)
	#m="CANARA BANK"
	for h in soup.findAll('table',attrs={"class" : "table table-bordered table-condensed articles"}):
	
		  r=h.getText()
		  if bank in r:
		  	str1=r
	return str1
		  

		#for y in h.findAll('td'):
			#print(y)