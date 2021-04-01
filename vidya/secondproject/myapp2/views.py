from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp2.forms import StudentForm
from myapp2.models import Student
#from django.contrib import messages

# Create your views here.

def hello(request):
	return HttpResponse("Iam from myapp2")

def register(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
		# #return HttpResponse("Done")
		# 	messages.success(request,request.POST['stuName']+' record stored successfully')
		# 	messages.info(request,"now you can add record")
		# 	return redirect ('/myapp2/register')
	form = StudentForm()
	return render(request,'myapp2/register.html',{'form':form})

def display(request):
	data = Student.objects.all()
	return render(request,'myapp2/display.html',{'data':data})


def update(request,id):
	data = Student.objects.get(id=id)
	if request.method =='POST':
		form = StudentForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
		#return HttpResponse("Done")
			return redirect ('/myapp2/display')
	form = StudentForm(instance=data)
	return render(request,'myapp2/update.html',{'form':form,'data':data})


def delete(request,id):
	ob = Student.objects.get(id=id)
	if request.method == 'POST':
		ob.delete()
		return redirect('/myapp2/display')
	return render(request,'myapp2/delete.html',{'info':ob})