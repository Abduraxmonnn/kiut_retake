# Generated by Django 4.2.3 on 2023-11-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retake', '0006_alter_retake_retake_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='retake',
            name='is_hide',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
