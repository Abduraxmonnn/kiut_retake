# Django
from django.contrib import admin

# Project
from apps.main.subjects.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'exam_type')
    list_display_links = ('name', )
    list_filter = ('exam_type', )
    search_fields = ('name', 'exma_type')
    ordering = ('id', )
