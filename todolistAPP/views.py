from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import ToDoSerializer
from models import ToDo, User
import datetime
from rest_framework import status
import json


def loginView(request):
    return render(request, 'login.html')


def index(request):
    c = {}
    try:
        Email = request.session['Email']
        id = request.session['id']
        c['Email'] = Email
        c['id'] = id
        return render(request, 'index.html', c)
    except:
        return HttpResponseRedirect('/login')


def registerView(request):
    return render(request, 'register.html')


class ToDoView(APIView):

    # get the whole toDoList
    def get(self, request):
        user = User.objects.filter(Email=request.session['Email'])
        user = user[0]
        todos = user.user_todo.all().order_by('time', 'finished')
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    # add an affair
    def post(self, request):
        try:
            type = request.data['type']
            if type == 'finish':
                id = request.data['id']
                todo = ToDo.objects.filter(id=id)[0]
                todo.finished = 1
                todo.save()
                return HttpResponse(json.dumps({'status': True, }))
            else:
                id = request.data['id']
                todo = ToDo.objects.filter(id=id)[0]
                todo.affair = request.data['affair']
                todo.time = request.data['time']
                todo.priority = request.data['priority']
                todo.save()
                return HttpResponse(json.dumps({'status': True, }))
        except:
            serializer = ToDoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save();
                return HttpResponse(json.dumps({'id': serializer.data['id'], }))
            return HttpResponse(json.dumps({'id': serializer.data['id'], }))

class ToDoViewAsPriority(APIView):
    # get the whole toDoList
    def get(self, request, priority):
        user = User.objects.filter(Email=request.session['Email'])
        user = user[0]
        todos = user.user_todo.filter(priority=priority).order_by('time', 'finished')
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)


class ToDoViewUpdateOrDelete(APIView):
    # delete an affair
    def delete(self, request, pk):
        try:
            todo = ToDo.objects.filter(id=pk)[0]
            todo.delete()
            return HttpResponse(json.dumps({'status': True, }))
        except:
            return HttpResponse(json.dumps({'status': False, }))


class ToDoViewOneDay(APIView):
    # get today toDolist
    def get(self, request, time):
        user = User.objects.filter(Email=request.session['Email'])
        user = user[0]
        todos = user.user_todo.filter(time=time).order_by('finished')
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)


class ToDoViewOneWeek(APIView):
    # get a week toDoList
    def get(self, request, time1, time2):
        user = User.objects.filter(Email=request.session['Email'])
        user = user[0]
        todos = user.user_todo.all().order_by('time', 'finished')
        t1 = datetime.date(*map(int, time1.split('-')))
        t2 = datetime.date(*map(int, time2.split('-')))

        def between(todo):
            return todo.time>=t1 and todo.time<=t2

        todos = filter(between, todos)
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)
