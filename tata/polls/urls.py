from ninja import NinjaAPI, ModelSchema, Schema
from polls.models import Player, Game
from django.utils import timezone

router = NinjaAPI()
class GameSchema(ModelSchema):
    class Meta:
        model = Game
        fields = [
            "id",
            "choice_text",
            "votes"
        ];

class PlayerSchema(ModelSchema):
    class Meta:
        model = Player
        fields = [
            "id",
            "name",
        ];
    games: list[GameSchema]

class AddGameSchema(Schema):
    name: str
    games: list[str]



@router.post("/start_game", response=GameSchema)
def start_game(request, add_game: AddGameSchema):
    player = Player.objects.create(name=add_game.name, pub_date=timezone.now())

    for game in add_game.games:    # pour rajouter l'affichage des games, il faut le rajouter à la base de Schema (pas dans meta)
        Game.objects.create(
            choice_text = game,
            player = player, 
        ) 
    return player

@router.get("/player/{player_id}", response=PlayerSchema)
def get(request, player_id: int):
    return Player.objects.get(pk=player_id)

