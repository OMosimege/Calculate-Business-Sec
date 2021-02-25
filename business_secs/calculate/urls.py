from django.urls import path

from .views import Business_SecsViewSet

app_name = "business_seconds_calculator"

urlpatterns = [
    url(r'^result/(?P<pk>[0-9]+)$',
    views.Business_SecsViewSet.as_view(),
    name=views.Business_SecsViewSet.name),
]