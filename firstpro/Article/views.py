from django.shortcuts import render,redirect
from .models import Article
# Create your views here.
def artlist(request):
	a=Article.objects.all()
	return render(request,"Article/artlist.html", {'data':a})
def artdetail(request,pk):
	a=Article.objects.get(id=pk)
	return render(request,"Article/artdetail.html",{'data':a})
def artdelete(request,pk):
	a=Article.objects.get(id=pk)
	a.delete()
	return redirect(artlist)
def artcreate(request):
	if request.method=="POST":
		s=Article()
		s.title=request.POST['t']
		s.body=request.POST['b']
		s.author=request.POST['a']
		s.save()
		return redirect('artlist')
	return render(request,'Article/create.html')
def artupdate(request,pk):
	a=Article.objects.get(id=pk)
	if request.method=="POST":
		a.title=request.POST['t']
		a.body=request.POST['b']
		a.author=request.POST['a']
		a.save()
		return redirect('artlist')
	return render(request,'Article/update.html',{'data':a})