from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"hotels", views.HotelListRetriveGenericViewSet, basename="hotel")
router.register(r"rooms", views.HotelRoomViewSet, basename="room")

urlpatterns = [
    path("", include(router.urls)),
    path("sign_up/", views.UserCreateView.as_view()),
    path("profile/<int:pk>/", views.UserDetailView.as_view()),
    path(
        "profile/<int:pk>/reservations/",
        views.UserDetailView.as_view(),
        {"action": "reservations"},
    ),
    path("create_hotel/", views.HotelCreateView.as_view()),
    path("delete_hotel/<int:pk>/", views.hotel_delete_view),
    path("update_hotel/<int:pk>/", views.hotel_update_view),
]
