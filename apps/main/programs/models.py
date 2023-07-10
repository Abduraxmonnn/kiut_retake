from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'
