# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.user.models import User


class Retake(models.Model):

    class LanguageTypes(models.TextChoices):
        UZBEK = "UZ", _("UZ")
        RUSSIAN = "RU", _("RU")
        ENGLISH = "EN", _("EN")

    language = models.CharField(max_length=2, choices=LanguageTypes.choices, default=LanguageTypes.UZBEK)
    user = User
