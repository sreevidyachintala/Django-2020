from django.shortcuts import render
from userApp.forms import UsersignupForm,DetailForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def signUp(request):
	if request.method == "POST":
		form = UsersignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Done")
	form = UsersignupForm()
	return render(request,"userApp/signUp.html",{'form':form})

def home(request):
	return render(request,'userApp/home.html',{})



@login_required
def profile(request,pk):
	data = User.objects.get(id=pk)
	if request.method=='POST':
		form = DetailForm(request.POST,request.FILES)
		print('i am')
		if form.is_valid():
			print('i am here'+str(pk) +' '+ request.POST['phoneNo'])
			try:
				f = form.save(commit=False)
				f.user_id = data.id.save()
				return HttpResponse('done.........')
			except:
				return HttpResponse('something wrong')
	form = DetailForm()
	return render(request,'userApp/profile.html',{'form':form,'data':data})