from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    designer = models.CharField(max_length=75)
    release_year = models.IntegerField()
    number_of_players = models.IntegerField()
    play_time = models.IntegerField()
    recommended_age = models.IntegerField()
    

