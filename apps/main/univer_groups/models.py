# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.main.faculty_directions.models import FacultyDirections


class UniverGroup(models.Model):
    class EducationTypes(models.TextChoices):
        FULL_TIME = "FULL_TIME", _("FULL_TIME")
        EVENING = "EVENING", _("EVENING")
        DISTANCE_LEARNING = "DISTANCE_LEARNING", _("DISTANCE_LEARNING")

    class LanguageTypes(models.TextChoices):
        UZBEK = "UZ", _("UZ")
        RUSSIAN = "RU", _("RU")
        ENGLISH = "EN", _("EN")

    name = models.CharField(max_length=255)
    level = models.SmallIntegerField(default=1, blank=True, null=True)
    type_education = models.CharField(max_length=17, choices=EducationTypes.choices, default=EducationTypes.FULL_TIME)
    language = models.CharField(max_length=2, choices=LanguageTypes.choices, default=LanguageTypes.UZBEK)
    faculty_dirs = models.ForeignKey(FacultyDirections, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.language}'

    class Meta:
        verbose_name = 'Univer Group'
        verbose_name_plural = 'Univer Groups'
