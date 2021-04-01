from django.shortcuts import render,redirect
from django.http import HttpResponse
from imageapp.forms import HotelForm 

# Create your views here.
def gallery(request):
	if request.method =='POST':
		form = HotelForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/success')
	form = HotelForm()
	return render(request,'gallery.html',{'form':form})

def success(request):
	return HttpResponse('successfully uploaded')

def display_image(request):
	if request.method == 'GET':
		hotels = Hotel.objects.all()
		return render(request,'display.html',{'hotels':hotels})