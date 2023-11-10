# Django
from django.contrib import admin

# Project
from apps.main.faculties.models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'dean']
    list_display_links = ['name']
    search_fields = ['name', ]
    ordering = ['-id']
