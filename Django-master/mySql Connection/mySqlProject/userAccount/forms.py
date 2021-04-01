from django.forms import ModelForm

from userAccount.models import UserRegister

class RegisterDetails(ModelForm):
	class Meta:
		model = UserRegister
		fields = '__all__'
