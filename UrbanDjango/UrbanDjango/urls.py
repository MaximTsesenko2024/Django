"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import Class_wiew, func_wiew
from task4.views import MainWiew, SelGame, Champion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', Class_wiew.as_view()),
    path('func/', func_wiew),
    path('main/', MainWiew.as_view()),
    path('select_game/', SelGame.as_view()),
    path('champion/', Champion.as_view())

]
