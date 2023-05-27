from rest_framework import viewsets, generics, mixins, status, permissions
from rest_framework.response import Response

from .models import HotelModel, HotelRoomModel
from .serializers import (
    HotelSerializer,
    HotelRoomSerializer,
    HotelRoomCreationSerializer,
)
from .mixins import AddHotelPermissionsMixin, IsAdminPermissionsMixin


class HotelListRetriveGenericViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    This is a generic viewset for list and retrive for HotelModel objects.
    """

    queryset = HotelModel.objects.all()
    serializer_class = HotelSerializer


class HotelCreateView(AddHotelPermissionsMixin, generics.CreateAPIView):
    """
    This is a CreateAPIView for creating a new hotel.
    """

    queryset = HotelModel.objects.all()
    serializer_class = HotelSerializer


class HotelUpdateDestroyView(
    IsAdminPermissionsMixin,
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


class HotelRoomViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides information about rooms.
    """

    serializer_class = HotelRoomSerializer
    queryset = HotelRoomModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = HotelRoomCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()
