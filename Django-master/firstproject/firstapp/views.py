from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
	return HttpResponse('<h2>Welcome to Django<br>Session</h2>')

def hello(request):
	return HttpResponse('<center>Hello Ambika Welcome to Django Project</center>')

def helloo(request,name):
	return HttpResponse('<h3>Hii</h3>' +name+ '<h3>Welcome to Django Session.</h3>')

def number(request,num):
	return HttpResponse('<h3>Hii</h3>' +str(num)+ '<h3>Welcome to Django Session.</h3>')

def message(request):
	return render(request,'firstapp/message.html',{})

def register(request):
	if request.method == "POST":
		name = request.POST['uname']
		mobileno = request.POST['mobno']
		email = request.POST['mailid']
		#print(name,email,mobileno)
		data= {'name':name,'phone':mobileno,'mail':email}
		#return HttpResponse('Done')
		return render(request,'firstapp/details.html',{'udata':data})
	return render(request,'firstapp/register.html',{})

def details(request):
	data = {'name':'Ambika','number':'1919'}
	return render(request,'firstapp/details.html',{'info':data})

def validation(request):
	if request.method == "POST":
		email = request.POST['mail']
		password = request.POST['pswd']
		if email == 'ambikapuvvula@gmail.com' and password == 'Ambika':
			return HttpResponse('Valid')
		else:
			return HttpResponse('Invalid')
	return render(request,'firstapp/validate.html',{})

def scboard(request):
	if request.method == "POST":
		team1 = request.POST.get('team1')
		team2 = request.POST.get('team2')
		if team1 is  not None:
			t1val = int(request.POST.get('t1val'))+ 1
			t2val = int(request.POST.get('t2val'))
		else:
			t1val = int(request.POST.get('t1val'))
			t2val = int(request.POST.get('t2val'))+ 1
		scores = {'t1val':t1val,'t2val':t2val}
		return render(request,'firstapp/scboard.html',scores)

	return render(request,'firstapp/scboard.html',{})

def basicgame(request):
	return render(request,'firstapp/basicgame.html',{})