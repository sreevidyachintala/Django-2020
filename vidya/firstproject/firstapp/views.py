xfrom django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
	return HttpResponse("<h2>Welcome to django<br>Session</h2>")


def hello(request,name):
	return HttpResponse('<h2>hi</h2>'+name+ '<h2>Welcome to django Session</h2>')


def rollno(reg,id):
	txt="<h2>your rollno is {}</h2>".format(id)
	return HttpResponse(txt)


def message(request):
	return render(request,"firstapp/message.html",{})


def register(request):
	if request.method=="POST":
		name=request.POST['uname']
		mobileno=request.POST['mbno']
		email=request.POST['email']
		#print(name)
		udata={'name':name,'phone':mobileno,'email':email}
		return render(request,'firstapp/details.html',{'udata':udata})
		#return HttpResponse('Done')
	return render(request,'firstapp/register.html')


def details(request):
	data={"name":"vidya","rollno":528}
	return render(request,'firstapp/details.html',{'data':data})




def scboard(request):
	if request.method=="POST":
		team1=request.POST.get('team1')
		team2=request.POST.get('team2')
		if team1 is not None:
			t1val=int(request.POST.get('t1val'))+1
			t2val=int(request.POST.get('t2val'))
		else:
			t1val= int(request.POST.get('t1val'))
			t2val=int(request.POST.get('t2val'))+1
		scores={'t1val':t1val,'t2val':t2val}
		return render(request,"firstapp/scboard.html",scores)
		#print(type(t1val))
	return render(request,'firstapp/scboard.html',{})


def home(request):
	return render(request,'firstapp/home.html',{})