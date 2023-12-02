# Django
from django.db import models

# Project
from apps.user.models import User
from apps.main.subjects.models import Subject


class Fail(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField()
    subject_credit = models.IntegerField()
    semester = models.IntegerField()
    is_free = models.BooleanField(default=True)

    @property
    def subject__name(self):
        return self.subject.name

    @property
    def user__student_id(self):
        return self.user.student_id

    def __str__(self):
        return f'{self.subject__name} - {self.user__student_id} - {self.is_free}'

    class Meta:
        verbose_name = 'Fail'
        verbose_name_plural = 'Fails'
