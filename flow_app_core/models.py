from random import choices

from django.db import models


# Create your models here.
class PostageItemModel(models.Model):
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

    track_number = models.CharField(max_length=13, verbose_name='Track number')
    recipient_street = models.CharField(choices=STREETS, max_length=4, verbose_name='Recipient street')
    recipient_build = models.CharField(max_length=5, verbose_name='Recipient build')
    small_package = models.BooleanField(default=False, verbose_name='Small package')
    delivered_date = models.DateTimeField()

    def __str__(self):
        return f'{self.track_number}: {self.recipient_street}'

    class Meta:
        ordering = ['delivered_date']
        verbose_name = 'postage item'
        verbose_name_plural = 'Postage items'