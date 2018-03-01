"""Opinionitycs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('',views.redirect,name='redirect'),
    path('analyze/', include('analyze.urls')),
    path('admin/', admin.site.urls),
    path('login/',login, name='login'),
    path('logout/', logout, name='logout')
]