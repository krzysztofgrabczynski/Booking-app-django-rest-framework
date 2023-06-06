from rest_framework import permissions


class AddHotelPermission(permissions.DjangoModelPermissions):
    """
    Class permissions which can check if the user has permisison to create (using POST method) new objects of the HotelModel class.
    """

    perms_map = {
        "GET": [],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": [],
        "PATCH": [],
        "DELETE": [],
    }


class IsAdminPermission(permissions.DjangoModelPermissions):
    """
    Class permissions which can check if the user is a member of the 'AdminUser' group or is a superuser (have all permissions).
    """

    def has_permissions(self, request, view):
        user = request.user
        if not user.groups.filter(name="AdminUser").exists() or user.is_superuser:
            return False
        return super().has_permission(request, view)


class IsObjectOwnerPermission(permissions.BasePermission):
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')

    def has_object_permission(self, request, view, obj):
        if request.method in self.SAFE_METHODS:
            return True

        user = request.user
        if user.groups.filter(name="AdminUser").exists() or user.is_superuser:
            return True
        if user == obj.owner:
            return True
        return False
