from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response

from .renderers import UserJSONRenderer
from .serializer import (TaskSerializer, ProjectSerializer, LoginSerializer,
    UserRegistrationSerializer,
    UserSerializer, ProjectsCommentSerializer, TaskCommentSerializer)
from .models import Task, RegisterUser, Projects


class Index:
    def index(request):
        return render(request, 'main/index.html')

class About:
    def about(request):
        return render(request, 'main/about.html')

class TaskList:
    def tasklist(request):
        tasks = Task.objects.all()
        return render(request, 'Tasks/task_list.html',
                      {'tasks': tasks})


class ProjectList:
    def projectlist(request):
        projects = Projects.objects.all()
        return render(request, 'Projects/projects_list.html',
                      {'projects': projects})


class TaskListView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    renderer_classes = (UserJSONRenderer,)

    def get(self, request):
        return render(request, 'Tasks/create_task.html')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "tasks": serializer.data,
            })

    def notify_user(user_id, message):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'user_{user_id}',
            {
                'type': 'send_notification',
                'message': message
            }
        )

class ProjectsListView(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    renderer_classes = (UserJSONRenderer,)

    def get(self, request):
        return render(request, 'Projects/create_project.html')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "projects": serializer.data,
            })

# Регистрация
class UserRegistrationView(generics.CreateAPIView):
    queryset = RegisterUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    renderer_classes = (UserJSONRenderer,)

    def get(self, request):
        return render(request, 'main/register.html')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "tokens": {
                "refresh": str(RefreshToken.for_user(user)),
                "access": str(RefreshToken.for_user(user)),
            },
        })

# Авторизация
class UserLoginView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def get(self, request):
        return render(request, 'main/login.html')

    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Профиль
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return render(request, 'main/about.html')


# Чтение задачи
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.task_comments.all()
    comment_serializer = TaskCommentSerializer()
    return render(request, 'Tasks/task_detail.html',
                  {'task': task,
                   'comments': comments,
                   'comment_serializer': comment_serializer})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        serializer = TaskSerializer(request.POST, instance=task)
        if serializer.is_valid():
            serializer.save()
            return redirect('Tasks/task_detail', pk=task.pk)
    else:
        serializer = TaskSerializer(instance=task)
    return render(request, 'Tasks/create_task.html',
                  {'serializer': serializer})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'Tasks/task_confirm_delete.html',
                  {'task': task})


def task_add_comment(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        serializer = TaskCommentSerializer(request.POST)
        if serializer.is_valid():
            comment = serializer.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            return redirect('task_detail', pk=task.pk)
    return redirect('Tasks/task_detail', pk=task.pk)



# Чтение проектов
def project_detail(request, pk):
    projects = get_object_or_404(Projects, pk=pk)
    comments = projects.project_comments.all()
    comment_serializer = ProjectsCommentSerializer()
    return render(request, 'Projects/project_detail.html',
                  {'projects': projects,
                   'comments': comments,
                   'comment_serializer': comment_serializer})

def project_update(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        serializer = ProjectSerializer(request.POST, instance=project)
        if serializer.is_valid():
            serializer.save()
            return redirect('Projects/project_detail', pk=project.pk)
    else:
        serializer = TaskSerializer(instance=project)
    return render(request, 'Projects/create_project.html', {'serializer': serializer})


def project_delete(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('task_list')
    return render(request, 'Projects/project_confirm_delete.html', {'project': project})


def project_add_comment(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        serializer = ProjectsCommentSerializer(request.POST)
        if serializer.is_valid():
            comment = serializer.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('project_detail', pk=project.pk)
    return redirect('Projects/project_detail', pk=project.pk)



def task_list(request):
    tasks = Task.objects.all()


    created_after = request.GET.get('created_after')
    created_before = request.GET.get('created_before')
    if created_after:
        tasks = tasks.filter(date_create__gte=created_after)
    if created_before:
        tasks = tasks.filter(date_create__lte=created_before)


    updated_after = request.GET.get('updated_after')
    updated_before = request.GET.get('updated_before')
    if updated_after:
        tasks = tasks.filter(date_update__gte=updated_after)
    if updated_before:
        tasks = tasks.filter(date_update__lte=updated_before)


    period_after = request.GET.get('period_after')
    period_before = request.GET.get('period_before')
    if period_after:
        tasks = tasks.filter(period_execution__gte=period_after)
    if period_before:
        tasks = tasks.filter(period_execution__lte=period_before)

    # Сортировка
    sort_by = request.GET.get('sort_by')
    if sort_by == 'created':
        tasks = tasks.order_by('date_create')
    elif sort_by == '-created':
        tasks = tasks.order_by('-date_create')
    elif sort_by == 'updated':
        tasks = tasks.order_by('date_update')
    elif sort_by == '-updated':
        tasks = tasks.order_by('-date_update')
    elif sort_by == 'title':
        tasks = tasks.order_by('title')
    elif sort_by == '-title':
        tasks = tasks.order_by('-title')

    return render(request, 'main/task_list.html', {'tasks': tasks})


def send_email_view(request):
    if request.method == 'POST':
        subject = 'Тема вашего сообщения'
        message = 'Содержимое вашего сообщения'
        from_email = 'vadimyxll@gmail.com'
        recipient_list = ['recipient_email@example.com']

        send_mail(subject, message, from_email, recipient_list)
        return redirect('some_view')
    return render(request, 'main/send_email.html')