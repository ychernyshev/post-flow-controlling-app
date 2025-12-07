from django.shortcuts import render
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from flow_app_core.models import postageItemModel
from flow_app_core.serializers import PostageItemSerializer


# Create your views here.
class DataPostageItemViewSet(viewsets.ModelViewSet):
    queryset = postageItemModel.objects.all()
    serializer_class = PostageItemSerializer

    @action(detail=True, methods=['post'])
    def mark_delivered(self, request, pk=None):
        item = self.get_object()
        item.delivered_date = timezone.now()
        item.save()
        return Response(
            {"status": "marked as delivered", "id": item.id, "delivered_date": item.delivered_date},
            status=status.HTTP_200_OK
        )