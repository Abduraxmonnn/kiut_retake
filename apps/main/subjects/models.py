from django.db import models


class Subject(models.Model):
    TEST = 'TEST'
    WRITE = 'WRITE'

    EXAM_TYPES = (
        (TEST, 'TEST'),
        (WRITE, 'WRITE'),
    )

    name = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=5, choices=EXAM_TYPES)
    hide = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
