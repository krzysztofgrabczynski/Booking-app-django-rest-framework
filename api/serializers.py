from rest_framework.serializers import ModelSerializer

from .models import HotelModel, HotelRoomModel


class HotelSerializer(ModelSerializer):
    """
    This is main serializer for HotelModel 
    """

    class Meta:
        model = HotelModel
        fields = ["id", "hotel_name", "address", "rate"]


class HotelMiniInformationSerializer(ModelSerializer):
    """
    This is a seiralizer without information about hotel rooms (for HotelRoomSerializer).
    """

    class Meta:
        model = HotelModel
        fields = ["id", "hotel_name", "address", "rate"]

class HotelRoomSerializer(ModelSerializer):
    """
    This is main serializer for HotelRoomModel.
    """

    hotel = HotelMiniInformationSerializer(many=False)

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

class HotelRoomCreationSerializer(ModelSerializer):
    """
    This is a serializer for creating new room.
    """

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
