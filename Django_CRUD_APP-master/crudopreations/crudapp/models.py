from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    mobile=models.CharField(max_length=15)

    class Meta:
        db_table="person"


