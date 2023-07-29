# Generated by Django 4.2.3 on 2023-07-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('image', models.ImageField(upload_to='files/deans/%Y/%m', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Dean',
                'verbose_name_plural': 'Deans',
            },
        ),
    ]