from rest_framework import serializers
from NewApp.models import Game, Developer

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Game
        fields = ('GameId', 'GameName', 'GameType', 'ReleaseDate', 'GameDeveloper')

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Developer
        fields = ('DeveloperId', 'DeveloperName')