from rest_framework.permissions import BasePermission


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
