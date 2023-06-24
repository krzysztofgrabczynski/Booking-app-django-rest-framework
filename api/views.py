from django.contrib.auth.models import User

from rest_framework import viewsets, generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from .models import HotelModel, HotelRoomModel, RoomReservation
from .serializers import (
    UserSerializer,
    HotelSerializer,
    HotelRoomSerializer,
    HotelRoomCreationSerializer,
    HotelDetailSerializer,
)
from .mixins import (
    AddHotelPermissionMixin,
    IsAdminPermissionMixin,
    IsObjectOwnerPermissionMixin,
    AllowAnyPermissionMixin,
    IsProfileOwnerMixin,
)


class HotelListRetriveGenericViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    This is a generic viewset for list and retrive for HotelModel objects.
    """

    queryset = HotelModel.objects.all()
    serializer_class = HotelSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = HotelDetailSerializer(instance)
        return Response(serializer.data)


class HotelCreateView(AddHotelPermissionMixin, generics.CreateAPIView):
    """
    This is a CreateAPIView for creating a new hotel.
    """

    queryset = HotelModel.objects.all()
    serializer_class = HotelSerializer


class HotelUpdateDestroyView(
    IsAdminPermissionMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    This is a generic viewset for updating and deleting existing hotel. Only for admin users.
    """

    queryset = HotelModel.objects.all()
    serializer_class = HotelSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            f"Deleteing of the {instance} Hotel", status=status.HTTP_202_ACCEPTED
        )


hotel_update_view = HotelUpdateDestroyView.as_view({"put": "update"})
hotel_delete_view = HotelUpdateDestroyView.as_view({"delete": "destroy"})


class HotelRoomViewSet(IsObjectOwnerPermissionMixin, viewsets.ModelViewSet):
    """
    A viewset for CRUD operations on the HotelRoomModel and room reservation functionality.
    """

    serializer_class = HotelRoomSerializer
    queryset = HotelRoomModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = HotelRoomCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def reservation(self, request, *args, **kwargs):
        room = self.get_object()
        if room.is_available is False:
            return Response("Room is already booked")

        room.is_available = False
        room.save()
        RoomReservation.objects.update_or_create(user=request.user, room=room)
        return Response("Booking successful")


class UserCreateView(AllowAnyPermissionMixin, generics.CreateAPIView):
    """
    This is a CreateAPIView for User model. It creates a new user with valid auth_token.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def _create_token(self, user):
        token = Token.objects.create(user=user)
        return token

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if User.objects.filter(email=serializer.data["email"]).exists():
            return Response("User with this email already exists")

        username = serializer.data.get("username")
        email = serializer.data.get("email")
        password = serializer.data.get("password")

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        self._create_token(user)
        return Response(serializer.data)


class UserDetailView(IsProfileOwnerMixin, generics.RetrieveAPIView):
    """
    Class representing details about a user. User can check only his own profile and list the room reservations that he has made.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        action = self.kwargs.get("action")
        if action == "reservations":
            return self.reservations(self, *args, **kwargs)

        return self.retrieve(request, *args, **kwargs)

    @action(detail=True, methods=["GET"])
    def reservations(self, *args, **kwargs):
        reservations = RoomReservation.objects.filter(user=self.kwargs.get("pk"))
        rooms = HotelRoomModel.objects.filter(room_reservation__in=reservations)

        serializer = HotelRoomSerializer(rooms, many=True)
        return Response(serializer.data)
