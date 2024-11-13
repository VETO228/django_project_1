from django.shortcuts import render
from rest_framework import generics
from .serializer import TaskSerializer, RegSerializer, ProjectSerializer
from .models import Task, Register
from rest_framework.views import APIView


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class RegisterAPIView(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegSerializer


class ProjectsAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Projects'})