# Generated by Django 3.1.6 on 2021-02-08 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raterapi', '0004_auto_20210208_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='est_time',
            new_name='play_time',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='age',
            new_name='recommended_age',
        ),
    ]
