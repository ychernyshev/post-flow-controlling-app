from django.db import models


# Create your models here.
class postageItemModel(models.Model):
    track_number = models.CharField(max_length=13, verbose_name='Track number')
    recipient_street = models.CharField(max_length=20, verbose_name='Recipient street')
    delivered_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return f'{self.track_number}: {self.recipient_street}'

    class Meta:
        ordering = ['delivered_date']
        verbose_name = 'postage item'
        verbose_name_plural = 'Postage items'
