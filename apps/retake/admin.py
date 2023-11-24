# Django
from django.contrib import admin

from apps.retake.models import Retake, RetakeCase


@admin.register(RetakeCase)
class RetakeCaseAdmin(admin.ModelAdmin):
    list_display = ['case_index', 'case']
    list_display_links = ['case_index']


@admin.register(Retake)
class RetakeAdmin(admin.ModelAdmin):
    list_display = ['user', 'case', 'subject', 'language']
    list_display_links = ['user', 'subject']
    list_filter = ['language']
    search_fields = ['user_student_id', ]
    ordering = ['-id']

    def user_student_id(self, obj):
        return obj.user.student_id
