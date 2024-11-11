from rest_framework import serializers
from .models import Task, Register, Projects


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
