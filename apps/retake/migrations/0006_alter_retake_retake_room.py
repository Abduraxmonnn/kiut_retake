# Generated by Django 4.2.3 on 2023-11-28 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
        ('retake', '0005_alter_retake_retake_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retake',
            name='retake_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.room'),
        ),
    ]
