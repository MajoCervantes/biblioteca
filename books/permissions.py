from rest_framework.permissions import BasePermission, SAFE_METHODS


class BelongsGroup(BasePermission):
    group = ""

    def has_permission(self, request, view):
        print(view)
        return request.user.groups.filter(name=self.group).exists()


class IsLibrarian(BelongsGroup):
    message = "You don't have permissions for this view"
    group = "Librarian"


class IsMember(BelongsGroup):
    message = "You're not a Member, please login"
    group = 'Member'

# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
