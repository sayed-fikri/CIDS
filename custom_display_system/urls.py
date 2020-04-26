"""custom_display_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth system
    # path('signup/', views.signupuser, name='signupuser'),
    path('', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    # path('logout/', views.logoutuser, name='logoutuser'),

    #information app
    path('dashboard/', include('information.urls')),
]
