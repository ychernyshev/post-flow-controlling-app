from rest_framework import serializers

from flow_app_core.models import postageItemModel


class postageItemSerializer(serializers.ModelSerializer):
    model = postageItemModel
    fields = '__all__'

