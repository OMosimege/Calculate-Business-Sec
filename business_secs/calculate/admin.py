from django.contrib import admin

@admin.register(Business_Secs)
class Business_SecsAdmin(BaseEventAdmin):
    list_display = ("start_time", "end_time")

