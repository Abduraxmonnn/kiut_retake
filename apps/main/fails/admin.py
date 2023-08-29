# Django
from django.contrib import admin

# Project
from apps.main.fails.models import Fail


@admin.register(Fail)
class FailAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject__name', 'user__student_id', 'is_free')
    list_display_links = ('subject__name', )
    list_filter = ('is_free', )
    search_fields = ('subject__name', 'user__student_id')
    ordering = ['-id']
