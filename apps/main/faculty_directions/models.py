# Django
from django.db import models

# Program
from apps.main.faculties.models import Faculty


class FacultyDirections(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Faculty Directions'
        verbose_name_plural = 'Faculty Directions'
