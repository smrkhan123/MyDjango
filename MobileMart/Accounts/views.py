from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout,login
from django.core.files.storage import FileSystemStorage
from django.db import connection
# Create your views here.

def signupview(request):
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,"Accounts/signup.html",{'form':form})

def editpro(request):
    if request.method=="POST":
        u=request.POST['us']
        f=request.POST['first']
        l=request.POST['last']
        e=request.POST['email']
        m=request.POST['mobile']
        aa=request.POST['aadhar']
        add=request.POST['address']
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        c=connection.cursor()
        c.execute(f"""update auth_user set first_name='{f}',
        	last_name='{l}',email='{e}',mobile='{m}',aadhar='{aa}',
        	address='{add}',pic='{uploaded_file_url}' where username='{u}'""")
        return redirect('home')


        
    return render(request,"Accounts/editpro.html")    

def loginview(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,"Accounts/login.html",{'form':form})

def logoutview(request):
	logout(request)
	return redirect('home')

