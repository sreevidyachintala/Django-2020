from django.shortcuts import render
from django.http import HttpResponse
from projectapp.forms import UserPage,PasReset
from projectapp.models import LoginPage,ResetPasword
from django.core.mail import send_mail
from project1 import settings
import random

# Create your views here.

def hello(request):
	return HttpResponse('done')

# def register()

def login(request):
	if request.method=="POST":
		uname=request.POST['uname']
		password=''
		form = LoginPage(uname=uname,password=password)
		form.save()
		#link="http://localhost:8000/reset/"
		sub = 'Welcome To Portal'
		body = 'your temporary  password is: '+str(random.randint(11111,99999 ))
		reciever = request.POST['uname']
		sender = settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[reciever])
		return HttpResponse('please check your mail')
	form=UserPage()
	return render(request,'projectapp/login.html',{'form':form})

def reset(request):
	return render(request,'projectapp/reset.html',{})

def val(request):
	if request.method =='POST':
		uname=request.POST['uname']
		password=request.POST['password']
		data=LoginPage.objects.get(uname=uname,password=password)
		if data:
			return redirect('/val')
		return HttpResponse('Please give valid email and password')
	return render(request,'projectapp/login.html')

