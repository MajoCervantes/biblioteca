from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from core.models import LibraryPlace

from .models import Book, Rack, BookItem
from .serializers import BookItemSerializer, BookSerializer, LibrarySerializer, RackSerializer  # noqa E501


# Create your views here.

# ? Class Views
class BookList(APIView):

    def get(self, req):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, req):
        serializer = BookSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ? Generic Views
class LibraryListGeneric(generics.ListCreateAPIView):

    queryset = LibraryPlace.objects.all()
    serializer_class = LibrarySerializer


class LibraryDetailGeneric(generics.RetrieveUpdateDestroyAPIView):

    queryset = LibraryPlace.objects.all()
    serializer_class = LibrarySerializer


class BookListGeneric(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailGeneric(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RackList(APIView):

    def get(self, req):
        racks = Rack.objects.all()
        serializer = RackSerializer(racks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RackByCat(APIView):

    def get(self, req, key):
        print('----------------------------', key)

        rack = Rack.objects.filter(category__contains=key)
        serializer = RackSerializer(rack, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RackByNum(APIView):

    # ! un número de estante que nos ayuda a encontrar el libro físicamente

    def get(self, req, key):

        rack = Rack.objects.filter(id=key)
        serializer = RackSerializer(rack, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookItemListGeneric(generics.ListCreateAPIView):

    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer


class BookItemDetailGeneric(generics.RetrieveUpdateDestroyAPIView):

    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer


class Catalog(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ['contains'],
        'author': ['contains'],
        'subject': ['contains']
    }
