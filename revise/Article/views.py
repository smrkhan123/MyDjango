from django.shortcuts import render,redirect
from .models import Article

def list(request):
	a=Article.objects.all()
	return render(request,"Article/list.html",{'data':a})
def detail(request,pk):
	a=Article.objects.get(id=pk)
	return render(request,"Article/detail.html",{'data':a})
def delete(request,pk):
	a=Article.objects.get(id=pk)
	a.delete()
	return redirect('list')
def create(request):
	if request.method=="POST":
		s=Article()
		s.title=request.POST['t']
		s.body=request.POST['b']
		s.author=request.POST['a']
		s.save()
		return redirect('list')
	return render(request,"Article/create.html")
def update(request,pk):
	a=Article.objects.get(id=pk)
	if request.method=="POST":
		a.title=request.POST['t']
		a.body=request.POST['b']
		a.author=request.POST['a']
		a.save()
		return redirect('list')
	return render(request,"Article/update.html",{'data':a})
