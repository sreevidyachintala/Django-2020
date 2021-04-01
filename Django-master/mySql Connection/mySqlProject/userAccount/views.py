from django.shortcuts import render,redirect
from django.http import HttpResponse
from userAccount.models import UserRegister
from userAccount.forms import RegisterDetails
from django.core.mail import send_mail
from mySqlProject import settings

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegisterDetails(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			sub = 'hi'
			body = 'Iam from django App'
			receiver = request.POST['mailid']
			sender = settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			return redirect('/register')
	form = RegisterDetails()
	return render(request,'userAccount/register.html',{'form':form})
	#return HttpResponse("From register page")

def display(request):
	data = UserRegister.objects.all()
	return render(request,'userAccount/display.html',{'data':data})

def info(request,id=id):
	data = UserRegister.objects.get(id=id)
	if request.method == 'POST':
		form = RegisterDetails(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/display')
	form = RegisterDetails(instance=data)
	return render(request,'userAccount/info.html',{'form':form,'data':data})

