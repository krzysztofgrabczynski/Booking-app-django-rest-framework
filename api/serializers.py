from rest_framework.serializers import ModelSerializer

from .models import HotelModel, HotelRoomModel


class HotelRoomsSerializer(ModelSerializer):
    """
    This serializer is used to serialize data without information about hotel (for HotelSerializer).
    """

    class Meta:
        model = HotelRoomModel
        fields = [
            "id",
            "room_no",
            "capacity",
            "description",
            "price_per_night",
            "is_available",
        ]


class HotelSerializer(ModelSerializer):
    """
    This is main serializer for HotelModel.
    """

    hotel_room = HotelRoomsSerializer(many=True)

    class Meta:
        model = HotelModel
        fields = ["id", "hotel_name", "address", "rate", "hotel_room"]


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
