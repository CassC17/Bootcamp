from ninja import NinjaAPI
from events.api import router as events_router
# from tata.polls.urls import 

api = NinjaAPI()

api.add_router("/polls", polls)
