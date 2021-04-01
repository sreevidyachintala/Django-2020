from django.urls import path
from myapp2 import views
urlpatterns = [
	path('',views.hello,name='hello'),
	path('register',views.register,name='register'),
	path('display',views.display,name='display'),
	path('update/<int:id>',views.update,name='update'),
	path('delete/<int:id>',views.delete,name='delete'),
]