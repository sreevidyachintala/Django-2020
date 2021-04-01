from django.contrib import admin
from .models import Emp

# Register your models here.
#admin.site.register(Emp)

#admin.site.register(Emp1)

class Emptable(admin.ModelAdmin):
	list_display=['first_name','last_name','age']
admin.site.register(Emp,Emptable)
