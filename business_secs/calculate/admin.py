from django.contrib import admin
from .models import Business_Secs

@admin.register(Business_Secs)
class Business_SecsAdmin(admin.ModelAdmin):
    list_display = ("start_time", "end_time", "business_seconds")

