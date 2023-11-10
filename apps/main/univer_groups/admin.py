# Django
from django.contrib import admin

# Project
from apps.main.univer_groups.models import UniverGroup


@admin.register(UniverGroup)
class UniverGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty_dirs', 'level', 'language', 'type_education']
    list_display_links = ['name', 'faculty_dirs']
    list_filter = ['language', 'level', 'type_education']
    search_fields = ['name', ]
    ordering = ['-id']
