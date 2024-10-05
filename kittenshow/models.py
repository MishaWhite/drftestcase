from Tools.demo.mcast import sender
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class KittenBreed(models.Model):
    name = models.CharField('Название породы', max_length=150, unique=True)
    description = models.TextField('Описание породы')

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField('Наименование цвета/окраса', max_length=150, unique=True)

    def __str__(self):
        return self.name


class Kitten(models.Model):
    name = models.CharField('Кличка котёнка', max_length=150)
    breed = models.ForeignKey(KittenBreed, verbose_name='Порода', on_delete=models.PROTECT)
    color = models.ForeignKey(Color, verbose_name='Цвет/окрас', on_delete=models.PROTECT)
    age = models.IntegerField('Возраст, мес.')
    description = models.TextField('Описание')
    user_add = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    rate_count = models.IntegerField('Оценок', null=True, editable=False)
    rate = models.FloatField('Средняя оценка', null=True, editable=False)

    def __str__(self):
        return ' '.join([self.name, self.breed, self.age])

    class Meta:
        unique_together = ('name', 'age', 'breed', 'user_add')


class Rating(models.Model):
    class Rate(models.IntegerChoices):
        ONE = 1, '\U00002605'
        TWO = 2, '\U00002605' * 2
        THREE = 3, '\U00002605' * 3
        FOUR = 4, '\U00002605' * 4
        FIVE = 5, '\U00002605' * 5

    kitten = models.ForeignKey(Kitten, verbose_name='Котёнок', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)
    value = models.SmallIntegerField('Оценка', choices=Rate.choices)

    class Meta:
        unique_together = ('kitten', 'user')


@receiver(post_save, sender='kittenshow.Rating')
def update_kitten_rate(sender, **kwargs):
    """
    Обработка сигнала сохранения оценки для рассчёта средней оценки
    :param sender:
    :param kwargs:
    :return:
    """
    kitten = Kitten.objects.select_for_update().get(pk=kwargs.instance.kitten)
    rate_sum = kitten.rate * kitten.rate_count
    kitten.rate_count += 1
    kitten.rate = (rate_sum + kwargs.get("instance").value) / kitten.rate_count
    kitten.save()
