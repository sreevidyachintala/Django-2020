from django import forms
from crudapp.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields="__all__"

