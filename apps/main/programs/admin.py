# Django
from django.contrib import admin

# Project
from apps.main.programs.models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )
    ordering = ('id', )
