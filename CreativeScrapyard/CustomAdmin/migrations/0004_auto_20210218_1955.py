# Generated by Django 3.1.5 on 2021-02-18 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAdmin', '0003_auto_20210218_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badgeentries',
            old_name='badge_id',
            new_name='badge',
        ),
    ]