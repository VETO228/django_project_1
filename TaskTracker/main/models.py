from django.contrib.auth.models import AbstractUser
from django.db import models


class RegisterUser(AbstractUser):
    surname = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='default_avatar.png')
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, blank=True)
    projects = models.TextField(blank=True)
    token = None

    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    link_proj = models.CharField('Проект', max_length=100)
    link_author = models.CharField('Автор', max_length=100)
    status = models.CharField('Статус',
        choices=[("Grooming", "Grooming"), ("In Progress", "In Progress"), ('Dev', 'Dev'), ('Done', 'Done')],
        max_length=100)
    priority = models.CharField('Приоритет', max_length=100, blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now=True)
    period_execution = models.DateTimeField('Срок выполнения', blank=True, null=True)
    tester = models.CharField('Ответственный за тестировку', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class TaskComment(models.Model):
    task = models.ForeignKey(Task, related_name='task_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий {self.user} к {self.task}'


class Projects(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    date_create = models.DateTimeField('Дата создания', blank=True, null=True)
    date_update = models.DateTimeField('Дата обновления', blank=True, null=True)
    status = models.CharField('Статус', choices=[('Активен', 'Активен'), ('Архивирован', 'Архивирован')] ,max_length=100)

    def __str__(self):
        return self.title

class ProjectsComment(models.Model):
    project = models.ForeignKey(Projects, related_name='project_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий {self.user} к {self.project}'