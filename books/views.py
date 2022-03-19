from rest_framework import generics
# from rest_framework.response import Response
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


# Create your views here.

# ? Generic Views
class BookList(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def delete(self, req, *args, **kwargs):
    #     return self.destroy(req, *args, **kwargs)

    # ? Soft delete
    # def perform_destroy(self, instance):
    #     instance.status = "Lost"
    #     instance.save()


class Catalog(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ['contains'],
        'author': ['contains'],
        'subject': ['contains']
    }
