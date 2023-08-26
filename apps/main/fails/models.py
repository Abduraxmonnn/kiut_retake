# Django
from django.db import models

# Project
from apps.user.models import User
from apps.main.subjects.models import Subject


class Fail(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.subject.name} - {self.user.student_id} - {self.is_free}'

    class Meta:
        verbose_name = 'Fail'
        verbose_name_plural = 'Fails'
