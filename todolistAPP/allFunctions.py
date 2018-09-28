from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
import json
from serializers import UserSerializer

# json.loads() // str to json
# json.dumps() // json to str
from todolistAPP.models import User

import json


def loginCheck(request):
    print("login checking......")
    ret = {'status': False, 'message': ''}
    if request.method == 'POST':
        Email = request.POST.get('Email')
        pwd = request.POST.get('password')

        user = User.objects.filter(Email=Email, password=pwd)[0]

        if user:
            ret['status'] = True
            request.session['Email'] = Email
            request.session['id'] = user.id
        else:
            ret['message'] = 'fail to login'
        return HttpResponse(json.dumps(ret))

def registerCheck(request):
    print("register checking......")
    ret = {'status': False, 'message': ''}
    if request.method == 'POST':
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        pwd = request.POST.get('password')

        user = User.objects.filter(Email=Email)

        if not user:
            serializer = UserSerializer(data=request.POST)
            if serializer.is_valid():
                ret['status'] = True
                serializer.save()
            else:
                ret['message'] = 'register failed!'
        else:
            ret['message'] = 'this Email has been registered!'
        return HttpResponse(json.dumps(ret))



