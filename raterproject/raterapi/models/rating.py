from django.db import models
from django.db.models.deletion import CASCADE

class Rating(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)