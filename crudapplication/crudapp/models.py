from django.db import models

# Create your models here.
class Person(models.Model):
	Fname=models.CharField(max_length=20)
	Lname=models.CharField(max_length=20)