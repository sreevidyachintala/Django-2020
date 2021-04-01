from django.shortcuts import render,redirect
from django.http import HttpResponse
from Ambika.forms import UserDetails
from Ambika.models import User

# Create your views here.
def hello(request):
	return HttpResponse("Iam From Ambika App")

def registerform(request):
	if request.method == 'POST':
		formdata = UserDetails(request.POST)
		if formdata.is_valid():
			formdata.save()
			User.objects.filter(FirstName=request.POST['FirstName']).update(Pswd=Pswd)
			return HttpResponse("<h2>your Password is "+request.POST['FirstName']+'@123')
	formdata = UserDetails()
	return render(request,'Ambika/registerform.html',{'formdata':formdata})

def login(request):
	
	return HttpResponse("Done")

def displaydata(request):
	return render(request,'Ambika/displaydata.html',{})