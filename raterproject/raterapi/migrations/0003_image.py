# Generated by Django 3.1.6 on 2021-02-08 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raterapi', '0002_game_gamer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.gamer')),
            ],
        ),
    ]