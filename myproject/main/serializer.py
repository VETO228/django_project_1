from rest_framework import serializers
from .models import Task, Register


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'