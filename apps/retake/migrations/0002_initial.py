# Generated by Django 4.2.3 on 2023-11-10 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('retake', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retake',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.subject'),
        ),
    ]