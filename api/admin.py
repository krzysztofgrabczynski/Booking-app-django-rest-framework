from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import HotelModel, HotelRoomModel, RoomReservation


admin.site.register(HotelModel)
admin.site.register(HotelRoomModel)
admin.site.register(RoomReservation)

admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["id", "username", "email"]
