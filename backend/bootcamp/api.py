from ninja import NinjaAPI
from polls.api import router 
from game.api import router

api = NinjaAPI()

api.add_router("/polls/", "polls.api.router")
api.add_router("/game/", "game.api.router")
