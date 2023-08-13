# Generated by Django 4.2.3 on 2023-08-13 20:14

import apps.user.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('univer_groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('student_id', models.CharField(max_length=15, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('passport_number', models.CharField(max_length=9, unique=True)),
                ('passport_issue_date', models.DateField(null=True)),
                ('passport_expiry_date', models.DateField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=6)),
                ('nation', models.CharField(blank=True, default='UZBEK', max_length=100)),
                ('profile_image', models.ImageField(upload_to=apps.user.models.upload_image_to)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('fails', models.IntegerField(blank=True, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('univer_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='univer_groups.univergroup')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['id'],
            },
        ),
    ]
