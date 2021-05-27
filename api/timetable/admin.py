from django.contrib import admin
from .models import Timetable

@admin.register(Timetable)
class AchivmentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "start_time",
        "end_time", 
        "name",
        "description",
        )

