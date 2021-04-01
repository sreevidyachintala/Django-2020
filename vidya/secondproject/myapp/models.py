from django.db import models

# Create your models here.
class Emp(models.Model):
	empid = models.CharField(max_length=20)
	empName = models.CharField(max_length=10)
	empDesig = models.CharField(max_length=30)
	salary = models.FloatField()

	def __str__(self):
		return self.empid+' '+self.empName