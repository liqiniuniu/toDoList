from rest_framework import serializers
from models import User, ToDo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'Email', 'password')


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'user', 'affair', 'finished', 'priority', 'time')





