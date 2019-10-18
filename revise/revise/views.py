from django.shortcuts import render

def home(request):
	data=['lis1','lis2','lis3','lis4','lis5']
	return render(request, "home.html",{'data':data})
def about(request):
	return render(request, "about.html")