from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)

from .permissions import (
    AddHotelPermission,
    IsAdminPermission,
    IsObjectOwnerPermission,
    IsProfileOwnerPermission,
)


class AddHotelPermissionMixin:
    permission_classes = [AddHotelPermission]


class IsAdminPermissionMixin:
    permission_classes = [IsAdminPermission]


class IsObjectOwnerPermissionMixin:
    permission_classes = [IsAuthenticatedOrReadOnly, IsObjectOwnerPermission]


class IsProfileOwnerMixin:
    permission_classes = [IsAuthenticated, IsProfileOwnerPermission]


class AllowAnyPermissionMixin:
    permission_classes = [AllowAny]
