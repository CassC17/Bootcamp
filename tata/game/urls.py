from ninja import NinjaAPI, ModelSchema, Schema
from game.models import Game, Player

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
    players: list[PlayerSchema]


class PlayerSchema(ModelSchema):
    class Meta:
        model = Player
        fields = [
            "id",
            "name",
            "score"
        ];
    games: list[GameSchema]

class AddPlayerSchema(Schema):
    name: str
    players: list[str]


@api.post("/start_game/", response=GameSchema)
def start_game(request, game_id: int):
    return Game.objects.get(pk=game_id)

@api.get("/player/{player_id}", response=PlayerSchema)
def get(request, player_id: int):
    return Player.objects.get(pk=player_id)

# @api.post("/add_player", response=PlayerSchema)
# def add(request, add_player: AddPlayerSchema):
#     player = Player.objects.create(name=add_player.name)

#     for game in add_player.games:    # pour rajouter l'affichage des games, il faut le rajouter à la base de Schema (pas dans meta)
#         Game.objects.create(
#             name = name,
#             player = player, 
#         ) 
#     return player