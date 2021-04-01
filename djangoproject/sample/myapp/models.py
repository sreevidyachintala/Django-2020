from django.db import models

# Create your models here.
class Register(models.Model):
	fullname = models.CharField(max_length=50)
	email    = models.EmailField(max_length=50)
	rollNo   = models.CharField(max_length=10)

