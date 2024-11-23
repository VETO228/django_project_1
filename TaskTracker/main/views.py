from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView

from .forms import UserRegistrationForm
from .serializer import TaskSerializer, RegSerializer, ProjectSerializer, LogSerializer, TokenSerializer, \
    ProjectMemberSerializer
from .models import Task, RegisterUser, Projects, ProjectMember
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class Index:
    def index(request):
        return render(request, 'main/index.html')


class About:
    def about(request):
        return render(request, 'main/about.html')


class Register:
    def register(request):
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                return render(request, 'main/register_done.html', {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
        return render(request, 'main/register.html', {'user_form': user_form})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenSerializer

class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


# Участники проекта
class ProjectMemberListCreateView(generics.ListCreateAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


def task_list(request):
    tasks = Task.objects.all()

    # Фильтрация по дате создания
    created_after = request.GET.get('created_after')
    created_before = request.GET.get('created_before')
    if created_after:
        tasks = tasks.filter(created_at__gte=created_after)
    if created_before:
        tasks = tasks.filter(created_at__lte=created_before)

    # Фильтрация по дате обновления
    updated_after = request.GET.get('updated_after')
    updated_before = request.GET.get('updated_before')
    if updated_after:
        tasks = tasks.filter(updated_at__gte=updated_after)
    if updated_before:
        tasks = tasks.filter(updated_at__lte=updated_before)

    # Фильтрация по сроку выполнения
    due_after = request.GET.get('due_after')
    due_before = request.GET.get('due_before')
    if due_after:
        tasks = tasks.filter(due_date__gte=due_after)
    if due_before:
        tasks = tasks.filter(due_date__lte=due_before)

    # Сортировка
    sort_by = request.GET.get('sort_by')
    if sort_by == 'created':
        tasks = tasks.order_by('created_at')
    elif sort_by == '-created':
        tasks = tasks.order_by('-created_at')
    elif sort_by == 'updated':
        tasks = tasks.order_by('updated_at')
    elif sort_by == '-updated':
        tasks = tasks.order_by('-updated_at')
    elif sort_by == 'title':
        tasks = tasks.order_by('title')
    elif sort_by == '-title':
        tasks = tasks.order_by('-title')

    return render(request, 'main/about.html', {'tasks': tasks})