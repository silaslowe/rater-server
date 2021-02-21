"""View module for handling requests about games"""
from raterapi.models.gameCategory import GameCategory
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterapi.models import Game, Gamer, Category

class Games(ViewSet):
    """Level up games"""
        
    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized isinstance
        """

        gamer = Gamer.objects.get(user=request.auth.user)

        game = Game()
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.release_year = request.data["release_year"]
        game.number_of_players = request.data["number_of_players"]
        game.play_time = request.data["play_time"]
        game.recommended_age = request.data["recommended_age"]
        game_category = GameCategory.objects.get(pk=request.data["game"])
        game.gamer = gamer

        try:
            game.save()
            serializer = GameSerializer(game, context ={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """

        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.description = request.data["description"]
        game.designer = request.data["designer"]
        game.release_year = request.data["release_year"]
        game.number_of_players = request.data["number_of_players"]
        game.play_time = request.data["play_time"]
        game.recommended_age = request.data["recommended_age"]
        game.gamer = gamer

        game.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try: 
            game = Game.objects.get(pk=pk)
            game.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """

        games = Game.objects.all()

        game_objects = []
        
        serializer = GameSerializer(
            games, many=True, context={'request': request})

        game_array = serializer.data
        for od in game_array:
            game_objects.append(dict(od))
        for game in game_objects:
           
            category = Category.objects.filter(gamecategory__game=game["id"])
            
            categories = CategorySerializer(
            category, many=True, context={'request': request}
            )

            game["categories"] = categories.data

        print(serializer.data)    
        return Response(game_objects)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'release_year', 'number_of_players', 'play_time', 'recommended_age', 'gamer')

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Category
        fields = ('id', 'category')