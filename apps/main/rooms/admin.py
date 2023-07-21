# Django
from django.contrib import admin

# Project
from apps.main.rooms.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'build', 'number', 'type_room')
    list_display_links = ('build', )
    list_filter = ('build', 'type_room')
    search_fields = ('number', )
    ordering = ('id', )
