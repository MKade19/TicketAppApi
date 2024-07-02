#from channels.routing import ProtocolTypeRouter, URLRouter
#from django.urls import re_path
#from chat.consumers import ChatConsumer

#websocket_urlpatterns = [
#    re_path(r'chat/', ChatConsumer.as_asgi()),
#]

# routing.py
from django.urls import re_path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'chat/', ChatConsumer.as_asgi()),
        ])
    )
})

websocket_urlpatterns = [
    re_path(r'chat/', ChatConsumer.as_asgi()),
]