from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    link_proj = models.TextField('Проект')
    link_author = models.TextField('Автор')
    status = models.TextField('Статус')
    priority = models.TextField('Приоритет')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now=True)
    period_execution = models.TextField('Срок выполнения')
    tester = models.TextField('Ответсвенный за тестировку')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'


class Register(models.Model):
    name = models.CharField('Имя пользователя', max_length=100)
    surname = models.CharField('Фамилия пользователя', max_length=100)
    avatar = models.ImageField()
    character = models.TextField('Роль на платформе')
    project = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        pass