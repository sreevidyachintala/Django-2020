from django.db import models

# Create your models here.
class LoginPage(models.Model):
	uname = models.EmailField(max_length=50,unique=True)
	password = models.CharField(max_length=20)

class ResetPasword(models.Model):
	oldpwd=models.CharField(max_length=20)
	newpwd=models.CharField(max_length=20)
	conpwd = models.CharField(max_length=20)
	