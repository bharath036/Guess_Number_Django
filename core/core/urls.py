"""
URL configuration for core project.

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
from home.views import index,contact,about,dynamic_url,project,request_product  #index is function defined in views.py

urlpatterns = [
    path('',index,name = 'index'),
    #path('home/',HomeView.as_view()),
    path('<id>/<name>',dynamic_url,name='dynamic_url'),
    path('request-product/',request_product,name = "request-product"),
    path('about/',about,name = 'about'),
    path('contact/',contact,name = 'contact'),
    path('admin/', admin.site.urls),
    path('project/',project,name="project")
]
