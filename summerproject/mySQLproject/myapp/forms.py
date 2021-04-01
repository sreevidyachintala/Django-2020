from django.forms import ModelForm
from myapp.models import UserRegister


class UserRegisterForm(ModelForm):
	class Meta:
		model = UserRegister
		fields = '__all__'