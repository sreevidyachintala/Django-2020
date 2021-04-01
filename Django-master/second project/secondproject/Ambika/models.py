from django.db import models

# Create your models here.
class User(models.Model):
	FirstName = models.CharField(max_length=20)
	LastName = models.CharField(max_length=20)
	UserName = models.CharField(max_length=20)
	Pswd = models.CharField(max_length=20)
	MailId = models.CharField(max_length=20)
	PhnNum = models.IntegerField()
	Age = models.IntegerField()