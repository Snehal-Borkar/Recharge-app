"""rechageapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from api_access import views 
from plan_api import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('loginuser/', views.handlelogin,name="login"),
    path('logout/', views.handlelogout, ),
    path('register/', views.handleregister),
    path('dashboard/', views.userhome),
    path('browseplans/', views.userhome),
    path('recharge/', views.recharge),
    path('plans/', v1.plans),
    path('rechargeplan/', v1.recharge_plan),
]
