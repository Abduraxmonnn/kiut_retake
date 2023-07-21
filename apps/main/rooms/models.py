# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    class BuildTypes(models.TextChoices):
        A_BUILD = "A_BUILD", _("A_BUILD")
        B_BUILD = "B_BUILD", _("B_BUILD")
        C_BUILD = "C_BUILD", _("C_BUILD")

    class RoomTypes(models.TextChoices):
        LECTURE = "LECTURE", _("LECTURE")
        PRACTICE = "PRACTICE", _("PRACTICE")

    build = models.CharField(
        max_length=7,
        choices=BuildTypes.choices,
        default=BuildTypes.A_BUILD,
    )
    number = models.IntegerField()
    type_room = models.CharField(
        max_length=8,
        choices=RoomTypes.choices,
        default=RoomTypes.LECTURE
    )

    def __str__(self):
        return f'{self.build} {self.number} {self.type_room}'

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
