#from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

# Create your views here.
def index(request):
	dic={}
	if request.method=="POST":
		upload_file=request.FILES['document']
		fs=FileSystemStorage()
		name=fs.save(upload_file.name,upload_file)
		dic['url']=fs.url(name)
	return render(request,'index.html',dic)

def book_list(request):
	books=Book.objects.all()
	return render(request,'book_list.html',{'books':books})

def upload_book(request):
	if request.method=="POST":
		form=BookForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('book_list')
	else:
		form=BookForm()
	return render(request,'upload_book.html',{'form':form})


