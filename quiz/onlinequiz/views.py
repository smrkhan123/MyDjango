from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from onlinequiz.models import Questions
# Create your views here.
def index(request):
	return render(request,'index.html')
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('dashboard')
		else:
			messages.error(request,"Username or Password is Incorrect")
			return redirect('login')
	return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return redirect('index')
def register(request):
	if request.method=="POST":
		first_name=request.POST['fname']
		last_name=request.POST['lname']
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		confirm_password=request.POST['confirm_password']
		if password==confirm_password:
			if User.objects.filter(username=username).exists():
				messages.error(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,'Email Taken')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
				user.save();
				messages.success(request,'Account Created Successfully')
				return redirect('login')
		else:
			message.error(request,'Password & Confirm Password Are Not Matching')
			return redirect('register')
	else:
		return render(request,'register.html')
def dashboard(request):
	return render(request,'dashboard.html')

def manage_users(request):
	if request.session._session:
		user=User.objects.all()
		return render(request,'manage_users.html',{'users':user})
	else:
		return render(request,'login.html')

def manage_questions(request):
	if request.session._session:
		question=Questions.objects.all()
		return render(request,'manage_questions.html',{'question':question})
	else:
		return render(request,'login.html')

def add_question(request):
	if request.session._session:
		if request.method=="POST":
			question=request.POST['question']
			option1=request.POST['option1']
			option2=request.POST['option2']
			option3=request.POST['option3']
			option4=request.POST['option4']
			right_answer=request.POST['right_answer']
			if Questions.objects.filter(questions=question).exists():
				messages.error(request,'Questions Already Exists Please change the question')
			else:
				question_data=Questions(questions=question,choice1=option1,choice2=option2,choice3=option3,choice4=option4,correct_answer=right_answer)
				question_data.save();
				messages.success(request,"Question Added Successfully")
				return redirect('manage_questions')
		return render(request,'add_question.html')
	else:
		return render(request,	'login.html')

def change_password(request):
	if request.method=="POST":
		form=PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'Your password was Successfully changed')
			return redirect('login')
		else:
			message.error(request,'Please correct the error below')
	else:
		form= PasswordChangeForm(request.user)
	return render(request,'change_password.html',{'form':form})


def delete(request,id):
	if request.session._session:
		User.objects.get(pk=id).delete()
		return redirect('manage_users')
	else:
		return render(request,'quiz.html')

def edit_question(request,id):
	if request.session._session:
		a=Questions.objects.get(pk=id)
		if request.method=="POST":
			a.questions=request.POST['question']
			a.option1=request.POST['option1']
			a.option2=request.POST['option2']
			a.option3=request.POST['option3']
			a.option4=request.POST['option4']
			a.correct_answer=request.POST['right_answer']
			a.save();
			messages.success(request,"Question Added Successfully")
			return redirect('manage_questions')
		return render(request,'edit_question.html',{'i':a})
	else:
		return render(request,'login.html')

def delete_question(request,id):
	if request.session._session:
		a=Questions.objects.get(pk=id)
		a.delete()
		return redirect('manage_questions')
	else:
		return render(request,'login.html')


def edit_user(request,id):
	if request.session._session:
		a=User.objects.get(pk=id)
		if request.method=="POST":
			a.username=request.POST['username']
			a.first_name=request.POST['fname']
			a.last_name=request.POST['lname']
			a.email=request.POST['email']
			a.save();
			messages.success(request,"User Updated Successfully")
			return redirect('manage_users')
		return render(request,'edit_user.html',{'i':a})
	else:
		return render(request,'login.html')

def delete_user(request,id):
	if request.session._session:
		a=User.objects.get(pk=id)
		a.delete()
		return redirect('manage_users')
	else:
		return render(request,'login.html')


def quiz(request):
	if request.session._session:
		question=Questions.objects.all()
		count=Questions.objects.all().count()
		return render(request,'quiz.html',{'questions':question,'count':count})
	else:
		return render(request,'login.html')

def result(request):
	values =list(request.POST)
	keys = list(request.POST.items())
	n=1
	newlist = values[n:]
	newkey = keys[n:]

	values_data = Questions.objects.filter(pk__in = newlist).values().order_by('id')
	l=[]
	count=0
	fc=0
	for i in values_data:
		fc=fc+1
		for j in newkey:
			if int(i['id'])==int(j[0]):
				i.update({'your_answer':j[1]})
				print(i)
				l.append(i)
				if i['correct_answer'] == i['your_answer']:
					count=count+1
			else:
				pass
	percentage=(count/fc)*100
	print(percentage)
	print(count)
	print(l)
	return render(request,'result.html',{'post_data':l,'counts':count,'per':percentage,'fc':fc})