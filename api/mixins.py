from rest_framework import mixins

from .permissions import AddHotelPermissions, IsAdminPermissions


class AddHotelPermissionsMixin:
    permission_classes = [AddHotelPermissions]


class IsAdminPermissionsMixin:
    permission_classes = [IsAdminPermissions]
