from rest_framework import permissions

class RolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True