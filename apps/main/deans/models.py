# Django
from django.db import models


class Dean(models.Model):
    """
    Model representing University Deans.

    The Dean model stores information about the Deans of various universities faculties.
    Each Dean is associated with a specific university and may have additional details
    such as their full name, date of birth, and an image representing them.
    """
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    image = models.ImageField(upload_to='files/deans/%Y/%m', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Dean'
        verbose_name_plural = 'Deans'
