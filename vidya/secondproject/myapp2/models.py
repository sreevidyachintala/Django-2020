from django.db import models

# Create your models here.
class Student(models.Model):
	branches = [('CSE','cse'),
				('ECE','ece'),
				('MEC','mec'),
				('EEE','eee'),
				('IT','it')]
	stuid = models.CharField(max_length=20)
	stuName = models.CharField(max_length=30)
	branch = models.CharField(max_length=20,choices=branches)
	age = models.IntegerField()


