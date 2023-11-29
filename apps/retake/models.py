# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.user.models import User
from apps.main.subjects.models import Subject
from apps.main.rooms.models import Room


class RetakeCase(models.Model):
    case_index = models.IntegerField(unique=True)
    case = models.TextField()

    def __str__(self):
        return self.case

    class Meta:
        verbose_name = 'Retake Case'
        verbose_name_plural = 'Retake Cases'


class Retake(models.Model):
    class LanguageTypes(models.TextChoices):
        UZBEK = "UZ", _("UZ")
        RUSSIAN = "RU", _("RU")
        ENGLISH = "EN", _("EN")

    language = models.CharField(max_length=2, choices=LanguageTypes.choices, default=LanguageTypes.UZBEK)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    case = models.ForeignKey(RetakeCase, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    is_hide = models.BooleanField(blank=True, null=True, default=False)
    retake_date = models.DateField(blank=True, null=True)
    retake_time = models.TimeField(blank=True, null=True)
    retake_room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.user.student_id} {self.case.case} {self.subject.name} {self.language}'

    class Meta:
        verbose_name = 'Retake'
        verbose_name_plural = 'Retakes'
