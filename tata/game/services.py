from django.db import models
from game.models import Game, Player


def create_game(game_name: str, players: list[str]):
    game = Game.object.create(name=game_name)
    # game  = Game(name = game_name) 
    # game.save()  --> AVENTAGE on peut surcharger la méthode save()

    for name in players:
        Player.objects.create(name = name, gmae = game)


def get_players(game_id): # grace au related name 
    game = Game.objects.get(pk=game_id)
    players = game.players.all() # renvoi un query set
    return players
    # AUTRE METHODE: return Player.objects.filter(game=game_id)

def update_score(player_id, score):
    player = Player.objects.get(pk=player_id)
    player.score = score
    player.save()
    return player

def get_winners():
    # should return all winners, closest to 21, it can have more than 1 winner
    game = Game.objects.get 