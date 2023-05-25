from rest_framework import viewsets
from rest_framework.response import Response

from .models import HotelModel, HotelRoomModel
from .serializers import HotelSerializer, HotelRoomSerializer


class HotelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides information about hotels
    """
    serializer_class = HotelSerializer
    queryset = HotelModel.objects.all()


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class HotelRoomViewSet(viewsets.ModelViewSet):
    serializer_class = HotelRoomSerializer
    queryset = HotelRoomModel.objects.all()

