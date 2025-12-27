from django.urls import path, include
from rest_framework import routers

import flow_app_core
from flow_app_core.views import DataPostageItemViewSet

router = routers.DefaultRouter()

router.register(r'postage', DataPostageItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', flow_app_core.views.search_engine, name='search_items'),
]
