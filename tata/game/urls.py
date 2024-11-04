from ninja import NinjaAPI, ModelSchema, Schema
from game.models import Game, Player
from django.utils import timezone

api = NinjaAPI()
class GameSchema(ModelSchema):
    class Meta:
        model = Game
        fields = [
            "id",
            "name",
            "turn",
            "ended"
        ];

class PlayerSchema(ModelSchema):
    class Meta:
        model = Player
        fields = [
            "id",
            "name",
            "score",
            "game"
        ];
    games: list[GameSchema]

class AddPlayerSchema(Schema):
    name: str
    players: list[str]



@api.post("/create_question", response=PlayerSchema)
def add(request, add_player: AddPlayerSchema):
    player = Player.objects.create(name=add_player.name)

    for game in add_player.games:    # pour rajouter l'affichage des games, il faut le rajouter à la base de Schema (pas dans meta)
        Game.objects.create(
            name = name,
            player = player, 
        ) 
    return player

@api.get("/player/{player_id}", response=PlayerSchema)
def get(request, player_id: int):
    return Player.objects.get(pk=player_id)