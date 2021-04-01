from django.contrib import admin
from .models import Employee

class employeeTable(admin.ModelAdmin):
	li = ['first_name','last_name']


# Register your models here.
admin.site.register(Employee,employeeTable)
