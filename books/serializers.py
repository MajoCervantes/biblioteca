from rest_framework import serializers
from core.models import LibraryPlace
from .models import Book, BookItem, Rack
from django.contrib.auth.models import User


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryPlace
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    library = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = '__all__'


class RackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rack
        fields = '__all__'


class BookItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookItem
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "password", "is_staff")
        # ? ocultar password al realizar petición
        extra_kwargs = {"password": {"write_only": True}}
