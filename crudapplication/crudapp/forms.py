from django.forms import ModelForm
from crudapp.models import Person

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields=['Fname','Lname']