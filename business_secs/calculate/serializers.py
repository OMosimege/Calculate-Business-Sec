from .models import Business_Secs
from rest_framework import serializers


class Business_SecsSerializer(BaseEventSerializer):
    class Meta:
        model = Business_Secs
        fields = "__all__"
