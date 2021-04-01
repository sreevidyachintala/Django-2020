from django.urls import path
from Ambika import views
urlpatterns = [
	path('',views.hello,name='hello'),
	path('registerform/',views.registerform,name='registerform'),
	path('login/',views.login,name='login'),
	path('displaydata/',views.displaydata,name='displaydata'),
]