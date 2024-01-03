from django.db import models

# Create your models here.

class Game(models.Model):
    GameId = models.AutoField(primary_key=True)
    GameName = models.CharField(max_length = 500)
    GameType = models.CharField(max_length = 500)
    ReleaseDate = models.DateField()
    GameDeveloper = models.CharField(max_length = 500)


class Developer(models.Model):
    DeveloperId = models.AutoField(primary_key=True)
    DeveloperName = models.CharField(max_length=500)
    