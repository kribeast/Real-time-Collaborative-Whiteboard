# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.urls import path
# from chatboard.consumers import BoardConsumer

# application = ProtocolTypeRouter({
#     'websocket': AllowedHostsOriginValidator(
#         URLRouter([
#                 path('', BoardConsumer)
#         ])
#     )

# })

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]