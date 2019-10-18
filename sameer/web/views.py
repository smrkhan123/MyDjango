from django.shortcuts import render,redirect
from .models import Destination 
from django.core.files.storage import FileSystemStorage
def index(request):
	destination = Destination.objects.all()
	return render(request,'web/index.html',{'destination':destination})
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
def edit(request,id):
	a=Destination.objects.get(pk=id)
	if request.method=="POST":
		a.name=request.POST['name']
		if a.img == "":
			pass
		else:
			a.img=request.FILES['document']
		a.desc=request.POST['desc']
		a.price=request.POST['price']
		a.offer=request.POST.get('offer','') == 'on'
		a.save()
		return redirect('index')
	return render(request,'web/edit.html',{'a':a})
def delete(request,id):
	a=Destination.objects.get(pk=id)
	a.delete()
	return redirect('index')
def add(request):
	if request.method=="POST":
		a=Destination()
		a.name=request.POST['name']
		if a.img != "":
			a.img=request.FILES['image']
		else:
			pass
		a.desc=request.POST['desc']
		a.price=request.POST['price']
		#a.offer=request.POST.get('offer')
		a.offer= request.POST.get('offer', '') == 'on'
		a.save()
		return redirect("/")
	else:
		return render(request,'web/add.html')