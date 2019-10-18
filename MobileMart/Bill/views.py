from django.shortcuts import render,redirect
from random import randint
from django.db import connection
from django.contrib import messages
# Create your views here.
def addpay(request):
	if request.method=="POST":
		card=request.POST['card']
		hold=request.POST['hold']
		date=request.POST['date']
		month=request.POST['month']
		cvv=request.POST['cvv']
		user=request.user.username
		print(user)
		ra=randint(1000000000,9999999999)
		cart=request.session.get('cart',{})
		total=0
		count=0
		for i in cart:
			d=cart[i]
			c=connection.cursor()
			total+=float(d[2])
			count+=1
			c.execute(f"insert into bill values('{user}','{d[11]}','{d[0]}','{d[1]}','{d[2]}','{d[9]}','{card}','{hold}','{date}','{month}','{cvv}','{ra}')")
		messages.success(request,f"Your Payment of {total} for {count} mobiles is completed..")
		return redirect('home')

	return render(request,'Bill/adddpay.html')