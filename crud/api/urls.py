from django.urls import path, include
from crud.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('crud', views.RecordViewSet, basename='records')

urlpatterns = [
    path('',include(router.urls))
]