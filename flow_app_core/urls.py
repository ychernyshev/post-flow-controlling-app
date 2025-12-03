from django.urls import path, include
from rest_framework import routers

from flow_app_core.views import DataPostageItemViewSet

router = routers.DefaultRouter()

router.register(r'postage', DataPostageItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
