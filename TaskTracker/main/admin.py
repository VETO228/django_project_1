from django.contrib import admin
from .models import Task, RegisterUser, Projects


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'period_execution')


@admin.register(RegisterUser)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',)
    list_display_links = ('email', 'username')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'date_create')