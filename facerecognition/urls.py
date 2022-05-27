"""facerecognition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from facerec import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('changepass', views.changepass, name='changepass'),
    path('createdata', views.createdata, name='createdata'),
    path('train', views.train, name='train'),
    path('takeattendance', views.takeattendance, name='takeattendance'),
    path('generate_dataset', views.generate_dataset, name='generate_dataset'),
    path('train_classifier', views.train_classifier, name='train_classifier'),
    path('detect_face', views.detect_face, name='detect_face'),
    path('draw_boundary', views.draw_boundary, name='draw_boundary'),
    path('markattendance', views.markattendance, name='markattendance'),
    path('authenticateuser', views.authenticateuser, name='authenticateuser'),
    
  


    
]
