from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.

def addcom(request):
	if request.method=='POST':
		m=request.POST['com']
		c=connection.cursor()
		c.execute(f"insert into company(`mobile`) values('{m}')")
		messages.success(request,f"{m} is added to your database..")
		messages.success(request,"You can add stock ....")
		return redirect('home')
	else:
		return render(request,"Mobile/addcom.html")
	return render(request,"Mobile/addcom.html")

def addmob(request):
	if request.method=='POST':
		r=request.POST['mob']
		r1=request.POST['mod']
		r2=request.POST['pri']
		r3=request.POST['qua']
		r4=request.POST['cha']
		r5=request.POST['bat']
		r6=request.POST['hea']
		r7=request.POST['mem']
		r8=request.POST['dat']
		myfile = request.FILES['ima']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		ufu = fs.url(filename)
		c=connection.cursor()
		c.execute(f"""insert into mobile(mobile_name,model,price,quantity,
			charger,battery,headset,memory,datacable,pics) 
			values('{r}','{r1}','{r2}','{r3}','{r4}','{r5}','{r6}','{r7}',
			'{r8}','{ufu}')""")
		messages.success(request,"Successfully stock added....")
		return redirect('home')
	else:
		c=connection.cursor()
		c.execute("select DISTINCT(company_name) from company")
		r=c.fetchall()
	return render(request,"Mobile/addmob.html",{'m':r})	

def moblist(request):
	c=connection.cursor()
	c.execute(f"select * from mobile")
	r=c.fetchall()
	return render(request,"Mobile/moblist.html",{'data':r})

def mobdet(request,id):
	c=connection.cursor()
	c.execute(f"select * from mobile where id='{id}'")
	r=c.fetchone()
	return render(request,"Mobile/mobdet.html",{'data':r})

def filmob(request):
	c=connection.cursor()
	r=f"select * from mobile"
	if request.method=="POST":
		mob=request.POST['mob']
		mod=request.POST['mod']
		frm=request.POST['from']
		to=request.POST['to']
		if frm:
			r=f"select * from mobile where mobile_name like '%{mob}%' and model like '%{mod}%' and (price>={frm} and price<={to})"
		else:
			r=f"select * from mobile where mobile_name like '%{mob}%' and model like '%{mod}%'"
	c.execute(r)
	d=c.fetchall()
	return render(request,"Mobile/filmob.html",{'data':d})	

def cfilmob(request):
	c=connection.cursor()
	r=f"select * from mobile"
	if request.method=="POST":
		mob=request.POST['mob']
		mod=request.POST['mod']
		frm=request.POST['from']
		to=request.POST['to']
		if frm:
			r=f"select * from mobile where mobile like '%{mob}%' and model like '%{mod}%' and (price>={frm} and price<={to})"
		else:
			r=f"select * from mobile where mobile like '%{mob}%' and model like '%{mod}%'"
	c.execute(r)
	d=c.fetchall()
	return render(request,"Mobile/cfilmob.html",{'data':d})		

@login_required(login_url='/accounts/login/')
def addcart(request,id):
	c=connection.cursor()
	c.execute(f"select * from mobile where id='{id}'")
	r=c.fetchone()
	cart=request.session.get('cart',{})
	cart[id]=r
	request.session['cart']=cart
	messages.success(request,f"Added to Cart...CheckOut to Confirm Process.")
	return redirect('cfilmob')

@login_required(login_url='/accounts/login/')
def viewcart(request):
	cart=request.session.get('cart',{})
	return render(request,"Mobile/viewcart.html",{'data':cart.values()})

@login_required(login_url='/accounts/login/')
def cartrem(request,id):
	print(request.session['cart'][str(id)])
	try:
		del request.session['cart'][str(id)]
	except Exception as e:
		print("Hello")
	request.session.modified=True	
	return redirect('viewcart')