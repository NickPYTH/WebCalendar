from django.contrib import admin
from .models import Monday, Thursday, Wednesday, Tuesday, Friday, Saturday, Sunday

@admin.register(Monday)
class MondayAdmin(admin.ModelAdmin):
    list_display = ("user", "case" ,"case_start", "case_end")
    list_filter = ("user", "case" )

@admin.register(Tuesday)
class TuesdayAdmin(admin.ModelAdmin):
    list_display = ("user", "case" ,"case_start", "case_end")
    list_filter = ("user", "case" )

@admin.register(Wednesday)
class WednesdayAdmin(admin.ModelAdmin):
    list_display = ("user", "case" ,"case_start", "case_end")
    list_filter = ("user", "case" )

@admin.register(Thursday)
class ThursdayAdmin(admin.ModelAdmin):
    list_display = ("user", "case" ,"case_start", "case_end")
    list_filter = ("user", "case" )

@admin.register(Friday)
class FridayAdmin(admin.ModelAdmin):
    list_display = ("user", "case" ,"case_start", "case_end")
    list_filter = ("user", "case" )

@admin.register(Saturday)
class SaturdayAdmin(admin.ModelAdmin):
    list_display = ("user", "case" ,"case_start", "case_end")
    list_filter = ("user", "case" )

@admin.register(Sunday)
class SundayAdmin(admin.ModelAdmin):
    list_display = ("user", "case" ,"case_start", "case_end")
    list_filter = ("user", "case" )