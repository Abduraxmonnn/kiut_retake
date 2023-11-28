# Django
from django.contrib import admin

# Project
from apps.main.faculty_directions.models import FacultyDirections


@admin.register(FacultyDirections)
class FacultyDirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty']
    list_display_links = ['name']
    search_fields = ['name', ]
    ordering = ['-id']
