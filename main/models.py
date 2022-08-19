from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField('Срок выполнения')
    location = models.CharField('Расположение', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"