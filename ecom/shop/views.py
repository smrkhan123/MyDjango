from django.shortcuts import render
from .models import Product,Contact
from django.http import HttpResponse
from math import ceil
# Create your views here.
def index(request):
	product = Product.objects.all()
	n=len(product)
	nslide=n//4 + ceil(n/4 - n//4)
	#params={'no_of_slides':nslide,'range':range(1,nslide),'product':product}
	#allprods=[[product,range(1,nslide),nslide],
		#		[product,range(1,nslide),nslide]]
	#params={'allprods':allprods}
	allprods=[]
	catprods=Product.objects.values('category','id')
	print(catprods)
	cats={item['category'] for item in catprods}
	print(cats)
	for cat in cats:
		prod=Product.objects.filter(category=cat)
		n=len(product)
		nslide=n//4 + ceil(n/4 - n//4)
		allprods.append([prod,range(1,nslide),nslide])
		params={'allprods':allprods}
	return render(request,'shop/index.html', params)
def about(request):
	return render(request,'shop/about.html')
def contact(request):
	if request.method=="POST":
		name=request.POST.get('name','')
		email=request.POST.get('email','')
		phone=request.POST.get('phone','')
		desc=request.POST.get('desc','')
		contact=Contact(name=name,email=email,phonr=phone,desc=desc)
		contact.save()
	return render(request,'shop/contact.html')
def tracker(request):
	return render(request,'shop/tracker.html')
def search(request):
	return render(request,'shop/search.html')
def productview(request,myid):
	product=Product.objects.filter(id=myid)
	return render(request,'shop/productview.html',{'product':product[0]})
def checkout(request):
	return render(request,'shop/checkout.html')
