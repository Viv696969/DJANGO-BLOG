"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='home'),
    path('article/<int:pk>',Article.as_view(),name='article'),
    path('create',Create.as_view(),name='create'),
    path('update/<int:pk>',Update.as_view(),name='update'),
    path('delete/<int:pk>',Delete.as_view(),name='delete'),
    path('category/<str:cat>',category,name='category'),
    path('like/<int:pk>',like,name='like'),
    path('createpofile',CreateProfile.as_view(),name='createprofile'),
    path('yourprofile',Yourprofile.as_view(),name='profile'),
    path('editprofile',Editprofile.as_view(),name='editprofile'),
    path('userprofile/<int:pk>',Userprofile.as_view(),name='userprofile'),


    #credentials
    path('register',Register.as_view(),name='register'),
    # path('login',L),
    path('blog/',include('django.contrib.auth.urls')),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
