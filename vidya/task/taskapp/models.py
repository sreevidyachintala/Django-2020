from django.db import models

# Create your models here.


class LoginForm(models.Model):
	email = models.EmailField(unique=True,max_length=30)
	password = models.CharField(max_length=20)
	datacheck = models.IntegerField(null=True)