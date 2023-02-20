from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from . import models


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return models.Employee.objects.create(**validated_data)


class SprintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sprint
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'
