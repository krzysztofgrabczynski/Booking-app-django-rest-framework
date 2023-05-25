from rest_framework.serializers import ModelSerializer

from .models import HotelModel, HotelRoomModel


class HotelSerializer(ModelSerializer):
    class Meta:
        model = HotelModel
        fields = ["id", "hotel_name", "address", "rate",]


class HotelRoomModel(ModelSerializer):
    hotel = HotelSerializer(many=False)

    class Meta:
        model = HotelRoomModel
        fields = [
            "id",
            "hotel",
            "room_no",
            "capacity",
            "description",
            "price_per_night",
            "is_available",
        ]
