# Generated by Django 4.2.3 on 2023-08-12 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
        ('deans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dean', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='deans.dean')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.program')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
    ]