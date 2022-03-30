from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import LibraryPlace
from .models import Book, Rack, BookItem
from .serializers import BookItemSerializer, BookSerializer, LibrarySerializer, RackSerializer, UserSerializer  # noqa E501
from .permissions import IsLibrarian, IsMember
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class CreateBookItems(APIView):
    def get(self, req):

        return render(req, 'book/create.html', {})

    def post(self, req):
        req_data = req.data

        if type(req_data) != dict:
            data = req_data.dict()
        else:
            data = req_data

        # * 1 create book
        book_author = data.get("author")
        book_isbn = data.get("isbn")
        book_title = data.get("title")
        book_abstract = data.get("abstract")
        book_editorial = data.get("editorial")
        book_publication_date = data.get("publication_date")
        book_language = data.get("language")
        book_number_of_pages = data.get("number_of_pages")
        book_category = data.get("category")

        new_book = Book(
            author=book_author,
            isbn=book_isbn,
            title=book_title,
            abstract=book_abstract,
            editorial=book_editorial,
            publication_date=book_publication_date,
            language=book_language,
            number_of_pages=book_number_of_pages,
            category=book_category,
        )

        new_book.save()
        # * end1 new book created

        # * 2 get rack
        book_rack = data.get("rack")
        rack_destination = Rack.objects.filter(category=book_rack).get()
        # * end2

        # * 3 create copies of the book
        book_price = int(data.get("price"))
        num_copies = int(data.get("copies"))

        new_book_instance = Book.objects.filter(id=new_book.id)

        copies = [
            BookItem(
                book=new_book_instance.get(),
                price=book_price,
                rack=rack_destination,

            ) for number in range(num_copies)
        ]
        print(copies)

        BookItem.objects.bulk_create(copies)
        # * end3 copies created in the db

        return Response(status=status.HTTP_200_OK)


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


class RackListGeneric(generics.ListCreateAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer


class RackDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer


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


class BookReservation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        return render(req, 'book/reservation.html', {})

    def post(self, req):
        req_data = req.data

        if type(req_data) != dict:
            data = req_data.dict()
        else:
            data = req_data
        # * aqui para reserva

        book_id = data.get("book")

        try:
            book_to_reserve = BookItem.objects.filter(
                Q(book=book_id) & Q(status="A")).first()
        except ObjectDoesNotExist:
            print("the book with given id doesn't exist.")

        if book_to_reserve == None:
            context = {
                "name": "user_name_here",
                "error": "no book in the moment.",
            }
            return render(req, 'book/reservation.html', context=context)
        else:
            book_to_reserve.status = "R"
            book_to_reserve.save()
            context = {
                "name": "user_name_here",
                "success": "all yours.",
            }
            return render(req, 'book/reservation.html', context=context)


class BorrowBook(APIView):

    def get(self, req):
        context = {
            "name": "user_name_here",
        }
        return render(req, 'book/borrow.html', context=context)

    def post(self, req):
        req_data = req.data

        if type(req_data) != dict:
            data = req_data.dict()
        else:
            data = req_data

        # * aqui para prestarlo

        book_id = data.get("book")
        book_format = data.get("format")
        date1 = parse_datetime(data.get("borrowed_date"))
        borrow_days = parse_datetime(data.get("due_date"))

        print(data, '---------------------------------')
        print(date1, borrow_days, '---------------------------------')

        try:
            to_be_borrowed = BookItem.objects.filter(Q(book=book_id) & Q(status="A"))[0]
        except ObjectDoesNotExist:
            context = {
                "name": "user_name_here",
                "error": "the book with given id doesn't exist.",
            }
            return render(req, 'book/borrow.html', context=context)

        to_be_borrowed.borrowed_date = make_aware(date1)
        to_be_borrowed.due_date = make_aware(borrow_days)
        to_be_borrowed.status = "B"
        to_be_borrowed.book_format = book_format
        to_be_borrowed.save()

        context = {
            "name": "user_name_here",
            "success": "its all yours",
        }
        # return Response(serializer.data,status=status.HTTP_200_OK)
        return render(req, 'book/borrow.html', context=context)


class BookItemListGeneric(generics.ListCreateAPIView):

    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer


class BookItemDetailGeneric(generics.RetrieveUpdateDestroyAPIView):

    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer


class BorrowedByUser(APIView):

    def get(self, req):
        return Response(status=status.HTTP_200_OK)


class Catalog(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ['contains'],
        'author': ['contains'],
        'category': ['contains']
    }


class ReturnBook(APIView):

    def get(self, req):
        return render(req, 'book/return.html', {})

    def post(self, req):

        req_data = req.data

        if type(req_data) != dict:
            data = req_data.dict()
        else:
            data = req_data

        book_id = data.get("book")
        print(book_id)

        # book_to_return = BookItem.objects.get(Q(book=book_id) & Q(user?))
        # book_to_return.status = "A"
        # book_to_return.borrowed_date = clean date
        # book_to_return.due_date = clean date
        # book_to_return.save()
        return render(req, 'book/return.html', {})


# ? User permissions
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # ? Only the librarian can see all users
    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [IsLibrarian()]

    # ? Overwrite method
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # ? Get the last created user
            user_list = list(User.objects.all().values())
            last_user = user_list.pop()['username']

            # ? add the last user to members group
            group = Group.objects.get(name="Member")
            user = User.objects.get(username=f'{last_user}')
            user.groups.add(group)

            return Response({"message": "User successful created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
