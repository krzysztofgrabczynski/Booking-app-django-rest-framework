from rest_framework import viewsets
from rest_framework.response import Response

from .models import HotelModel, HotelRoomModel
from .serializers import HotelSerializer, HotelRoomSerializer, HotelRoomCreationSerializer


class HotelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides information about hotels.
    """
    serializer_class = HotelSerializer
    queryset = HotelModel.objects.all()


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

