from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')
def login(request):
	return render(request,'login.html')
def register(request):
	return render(request,'register.html')
def contact(request):
	return render(request,'contact.html')
def newproducts(request):
	return render(request,'newproducts.html')
def myaccount(request):
	return render(request,'myaccount.html')
def location(request):
	return render(request,'location.html')
def faq(request):
	return render(request,'faq.html')
def shoppingcart(request):
	return render(request,'shoppingcart.html')
def specialoffer(request):
	return render(request,'specialoffer.html')
def news(request):
	return render(request,'news.html')