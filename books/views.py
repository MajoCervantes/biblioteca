from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q


from core.models import LibraryPlace

from .models import Book, Rack, BookItem
from .serializers import BookItemSerializer, BookSerializer, LibrarySerializer, RackSerializer  # noqa E501


# Create your views here.

# ? Class Views
class BookBy(APIView):

    def get(self, req, key):
        # DONE buscar por su título, autor, sujeto(abstract), categoría y fecha de publicación.
        # print('-------------------------------',key)
        books = Book.objects.filter(
            Q(author__contains=key)
            | Q(title__contains=key)
            | Q(abstract__contains=key)
            | Q(editorial__contains=key)
            | Q(category__contains=key)
            | Q(publication_date__contains=key)
            )
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, req, key):
        # aqui para prestarlo
        print(key)
        book = Book.objects.get()

        borrow = BookItem(
        # book = book
        # borrowed_date = 
        # due_date = 
        # price = 
        )

        # book.status = 'no dispo'
        # book.save()
        
        return Response(status=status.HTTP_200_OK)

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


# class BookDetailGeneric(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


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
        'category': ['contains']
    }
