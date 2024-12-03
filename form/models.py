from django.db import models
from django.contrib.auth.models import User


STATUS = (
    ('В ожидании', 'В ожидании'),
    ('В процессе', 'В процессе'),
    ('Завершено', 'Завершено')
        )


class Task(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, null=True)
    executor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    execution_status = models.CharField(max_length=15, choices=STATUS, verbose_name='Статус выполнения задачи', null=False)
    date_created = models.DateTimeField(verbose_name='Дата создания', null=False)
    date_completion = models.DateTimeField(verbose_name='Дата завершения', null=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='new_comment', null=True, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
