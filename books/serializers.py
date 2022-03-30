from attr import field
from rest_framework import serializers
from core.models import LibraryPlace
from .models import Book, BookItem, Rack
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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
        fields = [
            'borrowed_date',
            'due_date',
            'price',
            'book_format',
            'status',
            'book',
            'rack'
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        fields = ("id", "username", "password")
        # ? hide password
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # ? hash password
        validated_data["password"] = make_password(validated_data["password"])
        return super(UserSerializer, self).create(validated_data)
