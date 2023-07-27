# Django
from django.db import models


class Dean(models.Model):
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    image = models.ImageField(upload_to='files/deans/%Y/%m')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Dean'
        verbose_name_plural = 'Deans'
