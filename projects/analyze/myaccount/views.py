from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
	if request.method=="POST":
		f_name=request.POST["f_name"]
		l_name=request.POST["l_name"]
		email=request.POST["email"]
		password=request.POST["pass"]
		user=User.objects.create_user(username=email, first_name=f_name, last_name=l_name, email=email, password=password)
		user.save()
		messages.info(request,"Account Created Successfully")
		return redirect('login')
	return render(request,'web/register.html')
def login(request):
	if request.method=="POST":
		email=request.POST["email"]
		password=request.POST["pass"]
		user = auth.authenticate(username=email,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.success(request,"Username or Password is Incorrect")
			return redirect('login')
	return render(request,'web/login.html')
def logout(request):
	auth.logout(request)
	return redirect('index')

