from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Emp

# Create your views here.
def signup(request):
	if request.method == 'POST':
		# read data from the user
		empid = request.POST['empid']
		empName = request.POST['empName']
		empDesig = request.POST['empDesig']
		salary = request.POST['salary']
		# lefthand side values are database names and right hand side are py names
		obj = Emp(empid=empid,empName=empName,empDesig=empDesig,salary=salary)
		obj.save()
		return redirect('/showall')
		#return HttpResponse('done')



	return render(request,'myapp/signup.html')


def showall(request):
	data = Emp.objects.all()
	return render(request,'myapp/showall.html',{'data':data})# left hand side variable pass to htnl file