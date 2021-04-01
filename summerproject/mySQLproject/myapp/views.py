from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

from myapp.forms import *
from myapp.models import *
from django.core.mail import send_mail
from mySQLproject import settings 
# Create your views here.

def upload(request):
	if request.method =="POST":

		form = UserRegister(request.POST,request.FILES)
		if form .is_valid():
			form.save()
			sub = 'hii'
			body = 'i am comming from django app'
			receiver = request.POST['mailid']
			sender = settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			return HttpResponse("Image Uploaded.........")
	form = UserRegister()
	return render(request,'myapp/upload.html',{'form':form})

def displayimages(request):
	data=UserRegisterForm.objects.all()
	return render(request,'myapp/displayimages.html',{'data':data})
