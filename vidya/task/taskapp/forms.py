from django.forms import ModelForm

from taskapp.models import LoginForm

class UserLogin(ModelForm):
	class Meta:
		model = LoginForm
		fields ='__all__'