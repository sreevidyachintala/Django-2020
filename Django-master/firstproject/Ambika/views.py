from django.shortcuts import render
from django.http import HttpResponse
from Ambika.forms import UserDetails
from Ambika.models import User
from django.core.mail import send_mail
from firstproject import settings

# Create your views here.
def registerform(request):
	if request.method == 'POST':
		Pswd = request.POST['FirstName']+'@123'
		FirstName = request.POST['FirstName']
		LastName = request.POST['LastName']
		UserName = request.POST['UserName']
		MailId = request.POST['MailId']
		PhnNum = request.POST['PhnNum']
		Age = request.POST['Age']
		form = User(FirstName=FirstName,LastName=LastName,UserName=UserName,Pswd=Pswd,MailId=MailId,PhnNum=PhnNum,Age=Age)
		form.save()
		sub = 'hi'
		body = 'Your Password is '+Pswd
		receiver = request.POST['MailId']
		sender = settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[receiver])
		#return HttpResponse("<h2>your Password is "+Pswd)
	form = UserDetails()
	return render(request,'Ambika/registerform.html',{'form':form})

def login(request):
	if request.method == "POST":
		Uname = request.POST['Uname']
		Pwd = request.POST['Pwd']
		data = User.objects.all().filter(UserName=Uname,Pswd=Pwd)
		print(list(data))
		if data:
			return render(request,'Ambika/display.html',{'data':data})
		return HttpResponse("Please give Valid User Details")
	return render(request,'Ambika/login.html',{})

