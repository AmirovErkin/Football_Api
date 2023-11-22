from django.db import models


class Game(models.Model):
    date = models.DateField()
    teams = models.CharField(max_length=100)
    result = models.CharField(max_length=50)



class OldResult(models.Model):
    team = models.CharField(max_length=100)
    result = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Reminder(models.Model):
    email = models.EmailField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    link = models.URLField()
