# Django
from django.db import models

# Project
from apps.main.deans.models import Dean


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    dean = models.ForeignKey(Dean, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
