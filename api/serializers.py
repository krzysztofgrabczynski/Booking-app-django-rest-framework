from rest_framework.serializers import ModelSerializer, ValidationError

from django.contrib.auth.models import User

from .models import HotelModel, HotelRoomModel


class UserSerializer(ModelSerializer):
    """
    This is a serializer for User model. It is used in UserCreateView for creating new users.
    """

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "email": {"required": True},
            "password": {"required": True, "write_only": True},
        }

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("User with this email already exists")
        
        return email


class HotelSerializer(ModelSerializer):
    """
    This is main serializer for HotelModel
    """

    class Meta:
        model = HotelModel
        fields = ["id", "hotel_name", "address", "rate"]


class HotelRoomMiniSerializer(ModelSerializer):
    """
    This is a serializer with short information about room in a specific hotel (used for HotelDetailSerializer).
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


class HotelDetailSerializer(ModelSerializer):
    """
    This is a serializer for detail view (with informations about rooms in specific hotel).
    """

    hotel_room = HotelRoomMiniSerializer(many=True)

    class Meta:
        model = HotelModel
        fields = ["id", "hotel_name", "address", "rate", "hotel_room"]


class HotelRoomSerializer(ModelSerializer):
    """
    This is main serializer for HotelRoomModel.
    """

    hotel = HotelSerializer(many=False)

    class Meta:
        model = HotelRoomModel
        fields = [
            "id",
            "owner",
            "hotel",
            "room_no",
            "capacity",
            "description",
            "price_per_night",
            "is_available",
        ]
        read_only_fields = ["owner"]


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
