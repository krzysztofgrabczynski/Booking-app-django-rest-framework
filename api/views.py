from rest_framework import viewsets, generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import HotelModel, HotelRoomModel
from .serializers import (
    HotelSerializer,
    HotelRoomSerializer,
    HotelRoomCreationSerializer,
    HotelDetailSerializer,
)
from .mixins import (
    AddHotelPermissionMixin,
    IsAdminPermissionMixin,
    IsObjectOwnerPermissionMixi,
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


class HotelRoomViewSet(
    IsObjectOwnerPermissionMixi, viewsets.ModelViewSet
):  # IsObjectOwnerPermissionMixi,
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
        if room.is_available == False:
            return Response("Room is already booked")

        room.is_available = False
        room.save()
        return Response("Booking successful")
