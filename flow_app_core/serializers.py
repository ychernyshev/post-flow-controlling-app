from rest_framework import serializers

from flow_app_core.models import PostageItemModel


class PostageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostageItemModel
        fields = '__all__'

