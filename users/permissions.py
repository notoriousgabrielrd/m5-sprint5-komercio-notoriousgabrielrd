from rest_framework import permissions



class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.__dict__)
        return request.user == obj




class IsSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        return (
            request.user.is_authenticated and request.user.is_superuser
        )

                