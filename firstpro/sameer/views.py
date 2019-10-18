from django.shortcuts import render

# Create your views here.
def sam(request):
	data=['a','b','c','d']
	return render(request,'sameer/sam.html', {'data':data})
