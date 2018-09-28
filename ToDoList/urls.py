"""ToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from todolistAPP import views, tests, allFunctions

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/$', views.index),

    url(r'^login/', views.loginView),
    url(r'^login_check/', allFunctions.loginCheck),

    url(r'^register/', views.registerView),
    url(r'^register_check/', allFunctions.registerCheck),

    url(r'^index/todo/$', views.ToDoView.as_view()),
    url(r'^index/todo-(?P<time>[0-9]+-[0-9]+-[0-9]+)/$', views.ToDoViewOneDay.as_view()),
    url(r'^index/todo-(?P<priority>[1-3])/$', views.ToDoViewAsPriority.as_view()),
    url(r'^index/todo-updateOrDelete-(?P<pk>[0-9]+)/$', views.ToDoViewUpdateOrDelete.as_view()),
    url(r'^index/todo-(?P<time1>[0-9]+-[0-9]+-[0-9]+)&(?P<time2>[0-9]+-[0-9]+-[0-9]+)/$', views.ToDoViewOneWeek.as_view()),
]
