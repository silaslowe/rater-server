# Generated by Django 3.1.6 on 2021-02-08 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raterapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='raterapi.gamer'),
            preserve_default=False,
        ),
    ]
