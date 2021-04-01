from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userApp.models import Details


class UsersignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2',]


class DetailForm(ModelForm):
	class Meta:
		model = Details
		fields = ['age','phoneNo','gender','picture','date_of_birth']