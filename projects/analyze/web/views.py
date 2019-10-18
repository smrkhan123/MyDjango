from django.shortcuts import render,redirect
from .models import Destination
from django.core.files import File

def index(request):
	dest=Destination.objects.all()
	return render(request,'web/index.html',{'dest':dest})
def about(request):
	return render(request,'web/about.html')
def contact(request):
	return render(request,'web/contact.html')
def destinations(request):
	return render(request,'web/destinations.html')
def news(request):
	return render(request,'web/news.html')
def elements(request):
	return render(request,'web/elements.html')
def update(request,id):
	dest=Destination.objects.get(pk=id)
	if request.method=='POST':
		dest.name=request.POST['name']
		dest.desc=request.POST['desc']
		dest.price=request.POST['price']
		dest.img=request.FILES['image']
		dest.save()
		return redirect('index')
	return render(request,'web/update.html',{'dests':dest})
def delete(request,id):
	dest=Destination.objects.get(pk=id)
	dest.delete()
	return redirect('index')
def insert(request):
	if request.method=="POST":
		dest=Destination()
		dest.name=request.POST['name']
		dest.img=request.POST['img']
		dest.desc=request.POST['desc']
		dest.price=request.POST['price']
		dest.save()
		return redirect('index')
	return render(request,'web/insert.html')