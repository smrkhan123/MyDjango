from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.db import connection

# Create your views here.
def addcus(request):
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,"Customer/addcus.html",{'form':form})

def cuslist(request):
	query=connection.cursor()
	query.execute("select username,first_name,last_name,email,mobile,aadhar,address from auth_user where is_superuser='0'")
	s=query.fetchall()
	return render(request,"Customer/cuslist.html",{'data':s})

def cusdetail(request,u):
	query=connection.cursor()
	query.execute(f"select username,first_name,last_name,email,mobile,aadhar,address,pic from auth_user where username='{u}'")
	s=query.fetchone()
	return render(request,"Customer/cusdetail.html",{'data':s})	