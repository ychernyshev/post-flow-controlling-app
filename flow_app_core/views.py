from django.shortcuts import render
from rest_framework import viewsets

from flow_app_core.models import postageItemModel
from flow_app_core.serializers import PostageItemSerializer


# Create your views here.
class DataPostageItemViewSet(viewsets.ModelViewSet):
    queryset = postageItemModel.objects.all()
    serializer_class = PostageItemSerializer