from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('<center><h1>welcome django</h1></center>')

def sample11(request):
	return render(request,'myapp/sample1.html')

def register(request):
	if request.method=="POST":
		firstname=request.POST['firstname']
		email=request.POST['email']
		rollno=request.POST['rollno']
		#return HttpResponse('<h2>welcome'+firstname+'</h2>')
		form={'fname':firstname,'email':email,'rollnumber':rollno}
		return render(request,'myapp/show.html',{'form':form})
	return render(request,'myapp/register.html')
		