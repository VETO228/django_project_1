from django.shortcuts import render
from rest_framework import generics
from .serializer import TaskSerializer, RegSerializer
from .models import Task


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RegisterAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = RegSerializer

