from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from Messenger.consumers import ChatConsumer
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('home/<phone>/', ChatConsumer),
                ]
            )
        )
    )
})
