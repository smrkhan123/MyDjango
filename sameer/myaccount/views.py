from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.info(request,"Invalid Credential")
			return redirect('login')
	else:
		return render(request,"web/login.html")
	
def register(request):
	if request.method=="POST":
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		password1=request.POST['password1']

		user= User.objects.create_user(username=email, password=password1, email=email, first_name=first_name, last_name=last_name)
		user.save()
		messages.info(request,"Account Created Successfully")
		return redirect("register")
	else:
		return render(request,"web/register.html")

def logout(request):
	auth.logout(request)
	return redirect('index')