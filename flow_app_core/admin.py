from django.contrib import admin

from flow_app_core.models import postageItemModel


# Register your models here.
@admin.register(postageItemModel)
class postageItemAdmin(admin.ModelAdmin):
    list_dislpay = ['track_number', 'recipient_street', 'delivered_date']