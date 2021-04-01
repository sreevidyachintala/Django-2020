from django.shortcuts import render,redirect
from django.http import HttpResponse
from taskapp.models import LoginForm
from taskapp.forms import UserLogin
from django.core.mail import send_mail
from task import settings
import random

# Create your views here.
def home(request):
	return HttpResponse('Welcome all')


def login(request):
	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form:
			uemail=request.POST['email']
			upassword=str(random.randint(11111,99999))
			data=LoginForm(email=uemail,password=upassword,datacheck=0)
			data.save()
			sub="Welcome to our Portal"
			body="your temporary password"+upassword
			receiver=uemail
			sender = settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			return HttpResponse('Please check your email')
			return redirect('/loginmain')

		else:
			return HttpResponse("Already registered")
	form = UserLogin()
	return render(request,'taskapp/login.html',{'form':form})

def loginmain(request):
	if request.method == "POST":
		mail = request.POST['email']
		pwd = request.POST['password']
		data=LoginForm.objects.get(email=mail,password=pwd)
		if data.datacheck ==0:
			return redirect('/reset')
		else:
			return redirect('/display')
	return render(request,'taskapp/login.html')

def reset(request):
	if request.method == 'POST':
		oldpswd=request.POST['oldpassword']
		newpswd=request.POST['newpassword']
		confirmpswd=request.POST['cpassword']
		data=LoginForm.objects.get(password=oldpswd)
		data.datacheck = 1
		data.save()
		if newpswd != confirmpswd:
			return HttpResponse('doesnot match')
		else:
			data.password=confirmpswd
			data.save()
			return redirect('/display')
	return render(request,'taskapp/reset.html')

def display(request):
	return render(request,'taskapp/display.html')