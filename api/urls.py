from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'hotels', views.HotelViewset)
router.register(r'hotel_rooms', views.HotelRoomViewset)

url_patterns = [
    path("", include(router.urls))
]