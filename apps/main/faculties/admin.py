# Django
from django.contrib import admin

# Project
from apps.main.faculties.models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'program', 'dean']
    list_display_links = ['name', 'program']
    search_fields = ['name', ]
    ordering = ['-id']
