from random import choices

from django.db import models


# Create your models here.
class PostageItemModel(models.Model):
    track_number = models.CharField(max_length=13, verbose_name='Track number')
    recipient_street = models.ForeignKey('StreetsModel', db_index=True, on_delete=models.PROTECT, verbose_name='Recipient street')
    delivered_date = models.DateTimeField()

    def __str__(self):
        return f'{self.track_number}: {self.recipient_street}'

    class Meta:
        ordering = ['delivered_date']
        verbose_name = 'postage item'
        verbose_name_plural = 'Postage items'


class StreetsModel(models.Model):
    STREETS = [
        ('', ''),
        ('SHKI', 'Шкільна'),
        ('GONT', 'Гонти'),
        ('LUKR', 'Лесі Українки'),
        ('MAZE', 'Мазепи'),
        ('BOGU', 'Богуна'),
        ('HMEL', 'Б. Хмельницького'),
        ('LISN', 'Лісна'),
        ('PIDL', 'Підлісна'),
        ('STUS', 'Стуса'),
        ('FRAN', 'І. Франка'),
        ('SAGA', 'Сагайдачного'),
        ('SHEV', 'Т. Шевченка'),
        ('BAND', 'С. Бандери'),
    ]

    streets = models.CharField(choices=STREETS, max_length=4, default='', verbose_name='Вулиці')

    def __str__(self):
        return self.streets

    class Meta:
        verbose_name='вулиця'
        verbose_name_plural='Вулиці'
