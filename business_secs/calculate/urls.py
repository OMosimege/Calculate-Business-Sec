from django.urls import path, include
from . import views
from rest_framework import routers

from .views import Business_SecsViewSet

app_name = "business_seconds_calculator"

v2router = routers.DefaultRouter()
v2router.register("business_secs", Business_SecsViewSet, basename="business_secs")

urlpatterns = [
    path("business_secs/", include(v2router.urls)),
]