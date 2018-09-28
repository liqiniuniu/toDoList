from django.test import TestCase
from models import User, ToDo
# Create your tests here.
from django.shortcuts import render,HttpResponse
import datetime


def fun(request):
    # a = datetime.date.today()
    # print(a)
    # user = User(name='liqi', Email='liqi@qq.com', password='liqi1121')
    # user.save()
    # user = User.objects.filter(name='liqi')
    # user = user[0]
    # todo = ToDo(user=user, affair='homework', priority=1, time='2018-09-24')
    # todo.save()
    time = '2018-09-24'
    todo = ToDo.objects.filter(time=time)
    print(todo[0].time)
    print(1234)
    return HttpResponse('12345')

