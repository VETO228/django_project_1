from django.contrib import admin
from .models import Task, RegisterUser

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'period_execution')


@admin.register(RegisterUser)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',)
    list_display_links = ('email',)