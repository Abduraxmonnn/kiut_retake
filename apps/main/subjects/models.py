from django.db import models

from apps.main.departments.models import Department


class Subject(models.Model):
    TEST = 'TEST'
    WRITE = 'WRITE'

    EXAM_TYPES = (
        (TEST, 'TEST'),
        (WRITE, 'WRITE'),
    )

    name = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=5, choices=EXAM_TYPES)
    hide = models.BooleanField(default=False, blank=True, null=True)
    department = models.ManyToManyField(Department, related_name='departments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Subject, self).save(*args, **kwargs)
