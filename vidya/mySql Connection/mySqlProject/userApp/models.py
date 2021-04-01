from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Details(models.Model):
	vals = [('Male','Male'),('Female','Female')]
	age = models.IntegerField(null=True)
	phoneNo = models.CharField(max_length=10)
	gender = models.CharField(max_length=10,choices=vals)
	picture = models.ImageField(upload_to='profilepics/',null=True)
	date_of_birth = models.DateField(null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)	


	def __str__(self):
		return self.phoneNo

class EInfo(models.Model):
	salary = models.IntegerField(null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)


	#def __str__(self):
