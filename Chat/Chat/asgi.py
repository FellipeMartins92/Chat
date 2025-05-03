import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack   

import Messages.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Messages.routing.websocket_urlpatterns
        )
    )
})
