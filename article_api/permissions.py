from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsSubscriber(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.group == "subscriber"


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.email)
        return request.user.group == "author"
