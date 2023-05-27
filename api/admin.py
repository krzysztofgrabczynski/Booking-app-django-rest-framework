from django.contrib import admin

from .models import HotelModel, HotelRoomModel


admin.site.register(HotelModel)
admin.site.register(HotelRoomModel)
