# Generated by Django 4.2.3 on 2023-11-24 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
        ('retake', '0004_remove_retakecase_agreement_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retake',
            name='retake_room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='rooms.room'),
        ),
    ]