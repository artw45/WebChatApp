"""session_auth URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from django.views.generic import TemplateView
urlpatterns = [
   # path('admin/', admin.site.urls),
   path('admin/',admin.site.urls),
   path('api-auth/',include('rest_framework.urls')),
   path('accounts/',include('accounts.urls')),
   path('profile/',include('user_profile.urls')),
   path('friends/',include('friends.urls')),
   path('groups/',include('groups.urls')),
   path('chats/',include('chats.urls')),
   path('notification/',include('bnotify.urls')),
   path('groupmembers/',include('groupmembers.urls')),
   
   
]

urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]  #it allows react to take over routing & reg-ex for catching all requests
