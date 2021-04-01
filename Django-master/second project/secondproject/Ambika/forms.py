from django.forms import ModelForm

from Ambika.models import User

class UserDetails(ModelForm):
	class Meta:
		model = User
		fields = ['FirstName','LastName','UserName','MailId','PhnNum','Age']