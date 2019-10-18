from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import random
# Create your views here.
def index(request):
	so=requests.get("https://www.brainyquote.com/topics/life")
	soup=BeautifulSoup(so.text,"html.parser")
	li=[]
	for i in range(20):
		li.append(i)
	r=random.choice(li)
	print(soup.find_all(class_="clearfix")[r].a.get_text())
	question=soup.find_all(class_="clearfix")[r].a.get_text()
	print()


	return render(request,'index.html',{'questions':question})


