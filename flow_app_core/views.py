from django.shortcuts import render
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from flow_app_core.models import PostageItemModel
from flow_app_core.serializers import PostageItemSerializer


# Create your views here.
class DataPostageItemViewSet(viewsets.ModelViewSet):
    queryset = PostageItemModel.objects.all()
    serializer_class = PostageItemSerializer

    # Marking if the package was delivered
    @action(detail=True, methods=['post'])
    def mark_delivered(self, request, pk=None):
        item = self.get_object()
        item.delivered_date = timezone.now()
        item.save()
        return Response(
            {"status": "marked as delivered", "id": item.id, "delivered_date": item.delivered_date},
            status=status.HTTP_200_OK
        )

    # Searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['track_number', 'delivered_date']
    search_fields = ['recipient_street']
    ordering_fields = ['delivered_date']


def search_engine(request):
    query = request.GET.get('q')
    if query:
        results = PostageItemModel.objects.filter(name__icontains=query)
        data = [{"track_number": PostageItemModel.track_number, "recipient_street": PostageItemModel.recipient_street,
                 "delivered_date": PostageItemModel.delivered_date, "small_package": PostageItemModel.small_package,} for result in results]
