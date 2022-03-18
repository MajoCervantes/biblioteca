from rest_framework import serializers
from .models import Book, BookItem


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
