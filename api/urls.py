from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'hotels', views.HotelListRetriveGenericViewSet)
router.register(r'rooms', views.HotelRoomViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("create_hotel/", views.HotelCreateView.as_view()),
    path("delete_hotel/<int:pk>/", views.hotel_delete_view),
    path("update_hotel/<int:pk>/", views.hotel_update_view),
]