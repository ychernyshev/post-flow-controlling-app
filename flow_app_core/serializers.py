from rest_framework import serializers

from flow_app_core.models import postageItemModel


class PostageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = postageItemModel
        fields = '__all__'

