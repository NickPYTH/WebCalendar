from django.contrib import admin
from .models import ProxyUser

@admin.register(ProxyUser)
class ProxyUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        )
