from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class KittenBreed(models.Model):
    name = models.CharField('Название породы', max_length=150, unique=True)


class Color(models.Model):
    name = models.CharField('Наименование цвета/окраса', max_length=150, unique=True)


class Kitten(models.Model):
    name = models.CharField('Кличка котёнка', max_length=150)
    color = models.ForeignKey(Color, verbose_name='Цвет/окрас', on_delete=models.PROTECT)
    аge = models.IntegerField('Возраст, мес.')
    description = models.TextField('Описание')
    user_add = models.ForeignKey(User, on_delete=models.PROTECT)
