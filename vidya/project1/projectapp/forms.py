from django.forms import ModelForm

from projectapp.models import LoginPage,ResetPasword

class UserPage(ModelForm):
	class Meta:
		model = LoginPage
		fields = '__all__'

class PasReset(ModelForm):
	class Meta:
		model = ResetPasword
		fields = '__all__'