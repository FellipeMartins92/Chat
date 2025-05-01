from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Views.Home,name='Home'),
    path('',include("Users.urls")),
    path('',include("Groups.urls")),
    path('',include("Messages.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
