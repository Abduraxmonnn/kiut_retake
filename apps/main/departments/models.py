# Django
from django.db import models

# Project
from apps.main.deans.models import Dean
from apps.user.models import User


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    head_of_department = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
