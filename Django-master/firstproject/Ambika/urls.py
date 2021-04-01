from django.urls import path
from Ambika import views

urlpatterns=[
	path('registerform/',views.registerform,name='registerform'),
	path('login/',views.login,name='login'),
]