# Generated by Django 3.1.4 on 2021-02-12 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_auto_20210212_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='user_id',
            new_name='user',
        ),
    ]