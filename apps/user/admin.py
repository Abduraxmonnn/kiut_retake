# Django
from django.contrib import admin

# Project
from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'univer_group')
    list_display_links = ('student_id', 'full_name')
    list_filter = ('is_active', 'gender')
    search_fields = ('student_id', 'full_name', 'univer_group')
