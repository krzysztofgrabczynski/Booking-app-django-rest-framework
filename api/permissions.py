from rest_framework import permissions


class AddHotelPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': [],
        'PATCH': [],
        'DELETE': [],
    }

class IsAdminPermissions(permissions.DjangoModelPermissions):
    def has_permissions(self, request, view):
        user = request.user
        print(user.groups())
        print('s')
        if not user.groups.filter(name='AdminUser').exists() or user.is_superuser:
            return False
        return super().has_permission(request, view)