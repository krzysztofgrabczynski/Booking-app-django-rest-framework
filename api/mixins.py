from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import AddHotelPermission, IsAdminPermission, IsObjectOwnerPermission


class AddHotelPermissionMixin:
    permission_classes = [AddHotelPermission]


class IsAdminPermissionMixin:
    permission_classes = [IsAdminPermission]


class IsObjectOwnerPermissionMixi:
    permission_classes = [IsAuthenticatedOrReadOnly, IsObjectOwnerPermission]
