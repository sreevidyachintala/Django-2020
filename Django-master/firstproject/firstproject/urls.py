"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name='hi'),
    path('hello/',views.hello,name='hello'),
    path('helloo/<str:name>',views.helloo,name='helloo'),
    path('number/<int:num>',views.number,name='number'),
    path('message/',views.message,name='message'),
    path('register/',views.register,name='register'),
    path('details/',views.details,name='details'),
    path('validation/',views.validation,name='validation'),
    path('scboard/',views.scboard,name='scboard'),
    path('basicgame/',views.basicgame,name='basicgame'),
    path('Ambika/',include('Ambika.urls'))
]
