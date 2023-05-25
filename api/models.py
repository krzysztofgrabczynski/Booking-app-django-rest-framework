from django.db import models


class HotelModel(models.Model):
    hotel_name = models.CharField(max_length=32, unique=True, blank=False, null=False)
    address = models.CharField(max_length=128, blank=False, null=False)
    rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self) -> str:
        return self.hotel_name
    
    def __repr__(self) -> str:
        return self.__str__()