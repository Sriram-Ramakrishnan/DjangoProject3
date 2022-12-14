"""Project3 URL Configuration

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
from django.urls import path
from taskplanner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Auth 
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    #Task planner
    path('', views.home, name='home'),
    path('add/', views.addtask, name='addtask'),
    path('task/<int:task_pk>', views.viewtask, name='viewtask'),
    path('task/<int:task_pk>/complete', views.completetask, name='completetask'),
    path('completed/', views.viewcompletedtasks, name='viewcompletedtasks'),
    path('task/<int:task_pk>/delete', views.deletetask, name='deletetask'),
    path('task/<int:task_pk>/redo', views.redotask, name='redotask'),


]
