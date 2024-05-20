from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from users.views import UserViewSet 
from cities.views import CityViewSet
from stadiums.views import StadiumViewSet
from roles.views import RoleViewSet
from halls.views import HallViewSet
from seats.views import SeatViewSet
from events.views import EventViewSet
from applications.views import ApplicationViewSet
from authentication.urls import urlpatterns as auth_urls

BASE_URL = 'ticket-app/api/'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('cities', CityViewSet, basename='cities')
router.register('stadiums', StadiumViewSet, basename='stadiums')
router.register('roles', RoleViewSet, basename='roles')
router.register('halls', HallViewSet, basename='halls')
router.register('seats', SeatViewSet, basename='seats')
router.register('events', EventViewSet, basename='events')
router.register('applications', ApplicationViewSet, basename='applications')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include((router.urls, 'crud'))),
    path(BASE_URL + 'auth/', include((auth_urls, 'auth')))
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
