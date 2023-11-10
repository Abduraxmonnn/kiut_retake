# Generated by Django 4.2.3 on 2023-11-10 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty_directions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniverGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.SmallIntegerField(blank=True, default=1, null=True)),
                ('type_education', models.CharField(choices=[('FULL_TIME', 'FULL_TIME'), ('EVENING', 'EVENING'), ('DISTANCE_LEARNING', 'DISTANCE_LEARNING')], default='FULL_TIME', max_length=17)),
                ('language', models.CharField(choices=[('UZ', 'UZ'), ('RU', 'RU'), ('EN', 'EN')], default='UZ', max_length=2)),
                ('faculty_dirs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty_directions.facultydirections')),
            ],
            options={
                'verbose_name': 'Univer Group',
                'verbose_name_plural': 'Univer Groups',
            },
        ),
    ]
