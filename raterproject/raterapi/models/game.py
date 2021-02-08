from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=75)
    release_year = models.IntegerField()
    number_of_players = models.IntegerField()
    est_time = models.IntegerField()
    age = models.IntegerField()

