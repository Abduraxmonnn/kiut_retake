# Django
from django.contrib import admin

# Project
from apps.main.departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name', ]
    # ordering = ['-id']
