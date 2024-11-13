from django.core.validators import FileExtensionValidator
from django.db import models

from .base.services import get_path_upload_avatar, validate_size_image


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    link_proj = models.FileField('Проект')
    link_author = models.CharField('Автор', max_length=100)
    status = models.CharField('Статус', max_length=100)
    priority = models.CharField('Приоритет', max_length=100, blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now=True)
    period_execution = models.DateTimeField('Срок выполнения', blank=True, null=True)
    tester = models.CharField('Ответственный за тестировку', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'


class Register(models.Model):
    """Модель пользователя"""
    name = models.CharField('Имя пользователя', max_length=100, blank=True, null=True)
    surname = models.CharField('Фамилия пользователя', max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'gif']), validate_size_image])
    character = models.CharField('Роль на платформе', max_length=100, blank=True, null=True)
    project = models.FileField(blank=True, null=True)


    @property
    def is_authenticated(self):
        """Всегда возращает True. Это способ узнать, был ли пользователь аутентифицированы
        """
        return True


    def __str__(self):
        return self.name


    class Meta:
        pass


class Projects(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.CharField('Статус', max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        pass

