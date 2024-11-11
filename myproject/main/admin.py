from django.contrib import admin
from .models import Task, Register

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'period_execution')


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email',)
    list_display_links = ('email',)