from django.contrib import admin

from flow_app_core.models import PostageItemModel


# Register your models here.
@admin.register(PostageItemModel)
class PostageItemAdmin(admin.ModelAdmin):
    list_display = ['track_number', 'recipient_street', 'small_package', 'delivered_date']