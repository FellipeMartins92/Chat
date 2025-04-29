from django.contrib import admin
from django.urls import include, path
from . import Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Views.Home,name='Home'),
    path('',include("Users.urls")),
    path('',include("Groups.urls")),
    path('',include("Messages.urls")),
]
