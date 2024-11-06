from ninja import NinjaAPI
from polls.api import router as polls_router
from game.api import router as game_router

api = NinjaAPI()

api.add_router("/polls/", polls_router)
api.add_router("/game/", game_router)
