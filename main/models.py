from django.db import models


class Game(models.Model):
    article = models.CharField(max_length=25, verbose_name='Артикл')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.FileField(upload_to='img/card/')
    link = models.CharField(max_length=255, verbose_name='Якорь')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name
