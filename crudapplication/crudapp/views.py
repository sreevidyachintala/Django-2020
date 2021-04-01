from django.shortcuts import render,redirect
from django.http import HttpResponse
from crudapp.forms import PersonForm
from crudapp.models import Person


# Create your views here.
def register(request):
	if request.method=="POST":
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponse("Done")
	form = PersonForm()
	return render(request,'crudapp/register.html',{'form':form})

def display(request):
	data = Person.objects.all()
	return render(request,'crudapp/display.html',{'data':data})

def update(request,id):
	data = Person.objects.get(id=id)
	if request.method == 'POST':
		form = PersonForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/crudapp/display')
	form = PersonForm()
	print(form)
	return render(request,'crudapp/update.html',{'form':form,'data':data})

def delete(request,id):
	ob = Person.objects.get(id=id)
	if request.method == 'POST':
		ob.delete()
		return redirect('/crudapp/display')
	return render(request,'crudapp/delete.html',{'info1':ob})
