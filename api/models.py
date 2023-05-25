from django.db import models


class HotelModel(models.Model):
    hotel_name = models.CharField(max_length=32, unique=True)
    address = models.CharField(max_length=128)
    rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self) -> str:
        return self.hotel_name

    def __repr__(self) -> str:
        return self.__str__()


class HotelRoomModel(models.Model):
    hotel = models.ForeignKey(
        HotelModel, on_delete=models.CASCADE, related_name="hotel_room"
    )
    room_no = models.SmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    description = models.TextField(default="")
    price_per_night = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def _name(self) -> str:
        return f"{self.hotel.hotel_name} - room: {self.room_no}"

    def __str__(self) -> str:
        return self._name()

    def __repr__(self) -> str:
        return self._name()
