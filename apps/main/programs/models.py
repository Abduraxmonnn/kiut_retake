from django.db import models


class Program(models.Model):
    """
    This model used to save KIUT Programs just like `School Of Engineering`

    **Context**

    ``Program``
        An instance of :model:`apps.main.programs.Program`.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'
