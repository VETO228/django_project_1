from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    link_proj = models.TextField('Проект')
    link_author = models.TextField('Автор')
    status = models.TextField('Статус')
    priority = models.TextField('Приоритет')
    date_create = models.TextField('Дата создания')
    date_update = models.TextField('Дата обновления')
    period_execution = models.TextField('Срок выполнения')
    tester = models.TextField('Ответсвенный за тестировку')

    def __str__(self):
        return self.title