# Generated by Django 4.1.5 on 2023-01-26 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='member',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.RemoveField(
            model_name='member',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.RemoveField(
            model_name='member',
            name='status',
        ),
        migrations.RemoveField(
            model_name='member',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
    ]
