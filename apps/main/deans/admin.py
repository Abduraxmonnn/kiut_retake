# Django
from django.contrib import admin

# Project
from apps.main.deans.models import Dean


@admin.register(Dean)
class DeanAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('full_name', )
    search_fields = ('full_name', )
    ordering = ('id', )
