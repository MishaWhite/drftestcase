from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class KittenBreed(models.Model):
    name = models.CharField('Название породы', max_length=150, unique=True)
    description = models.TextField('Описание породы')


class Color(models.Model):
    name = models.CharField('Наименование цвета/окраса', max_length=150, unique=True)


class Kitten(models.Model):
    name = models.CharField('Кличка котёнка', max_length=150)
    breed = models.ForeignKey(KittenBreed, verbose_name='Порода', on_delete=models.PROTECT)
    color = models.ForeignKey(Color, verbose_name='Цвет/окрас', on_delete=models.PROTECT)
    age = models.IntegerField('Возраст, мес.')
    description = models.TextField('Описание')
    user_add = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return ' '.join([self.name, self.breed, self.age])

    class Meta:
        unique_together = ('name', 'age', 'breed', 'user_add')


class Rating(models.Model):
    kitten = models.ForeignKey(Kitten, verbose_name='Котёнок', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)
    #TODO: Добавить choices
    value = models.IntegerField('Оценка')

    class Meta:
        unique_together = ('kitten', 'user')

