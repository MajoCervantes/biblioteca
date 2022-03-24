from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.dateparse import parse_datetime
# from django.utils.timezone import make_aware



from core.models import LibraryPlace
from .models import Book, Rack, BookItem
from .serializers import BookItemSerializer, BookSerializer, LibrarySerializer, RackSerializer  # noqa E501


# Create your views here.

# ? Class Views
class CreateBookItems(APIView):
    def get(self, req):
        
        return render(req, 'book/create.html', {})

    def post(self, req):
        all_data = req.data.dict()

        #*create book
        book_author = all_data.get("author")
        book_isbn = all_data.get("isbn")
        book_title = all_data.get("title")
        book_abstract = all_data.get("abstract")
        book_editorial = all_data.get("editorial")
        book_publication_date = all_data.get("publication_date")
        book_language = all_data.get("language")
        book_number_of_pages = all_data.get("number_of_pages")
        book_category = all_data.get("category")

        new_book = Book(
            author = book_author,
            isbn = book_isbn,
            title = book_title,
            abstract = book_abstract,
            editorial = book_editorial,
            publication_date = book_publication_date,
            language = book_language ,
            number_of_pages = book_number_of_pages,
            # library = ,
            # category = book_category,
        )

        new_book.save()
        # * new book created


        # * create copies of the book
        book_rack = all_data.get("rack")
        book_status = all_data.get("status")
        book_price = int(all_data.get("price"))
        num_copies = int(all_data.get("copies"))


        new_book_instance = Book.objects.filter(id=new_book.id)


        copies = [ 
            BookItem( 
                book = new_book_instance.get(),
                price = book_price,
                # rack = book_rack,
                status = book_status,
            ) for number in range(num_copies)
        ]
        print(copies)

        BookItem.objects.bulk_create(copies)
        # * copies created in the db

        return Response(status=status.HTTP_200_OK)

class BookBy(APIView):

    def get(self, req, key):
        # DONE buscar por su título, autor, sujeto(abstract), categoría y fecha de publicación.
        # print('-------------------------------',key)
        books = Book.objects.filter(
            Q(author__contains=key)
            | Q(id=key)
            | Q(title__contains=key)
            | Q(abstract__contains=key)
            | Q(editorial__contains=key)
            | Q(category__contains=key)
            | Q(publication_date__contains=key)
            )
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

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

class BookReservation(APIView):

    def get(self, req):
        return render(req,'book/reservation.html',{})


    def post(self, req):
        # * aqui para reserva
        
        all_data = req.data.dict()
        book_id = all_data.get("book")

        # SELECT FROM bookItem WHERE book = book_to_reserve
        # AND status = A

        try:
            book_to_reserve = Book.objects.filter(id=book_id)
        except ObjectDoesNotExist:
            print("the book with given id doesn't exist.")

        book_status = book_to_reserve.values_list('status', flat=True).get(pk=book_id)

        if book_status == 'R' | 'B':
            print('already reserved. add user to queue')
        if book_status == 'A':
            print('reserved or u can take it RN')
        else:
            print("try with another book")

        # book_to_reserve.update(status='R')
        return Response(status=status.HTTP_200_OK)
        

            


class BorrowBook(APIView):

    def get(self, req):
        context={
            "name": "user_name_here",
        }
        return render(req,'book/borrow.html',context=context)


    def post(self, req):
        # * aqui para prestarlo

        all_data = req.data.dict()

        book_id = all_data.get("book")
        date1 = parse_datetime(all_data.get("borrowed_date"))
        borrow_days = parse_datetime(all_data.get("due_date"))
        borrow_pay = all_data.get("price")

        print(
            book_id,
            date1,
            borrow_days ,
            borrow_pay ,
            '---------------------------------------'
        )

        # try:
        #     to_be_borrowed = Book.objects.filter(id=book_id)
        # except ObjectDoesNotExist:
        #     context={
        #         "name": "user_name_here",
        #         "error": "the book with given id doesn't exist.",
        #     }
        #     return render(req,'book/borrow.html',context=context)


        


        # book_status = to_be_borrowed.values_list('status', flat=True).get(pk=book_id)

        # if book_status == 'A':

        #     # borrow = BookItem.objects.bulk_create(

        #     # )

        #     borrow = BookItem(
                
        #         book = to_be_borrowed.get(),
        #         # user = user in session,
        #         borrowed_date =  make_aware(date1),
        #         due_date = make_aware(borrow_days),
        #         price = borrow_pay,
        #         # book_format = ,
        #     )
        #     borrow.save()

        #     print('me llevaste', borrow)

        #     to_be_borrowed.update(status='B')

        #     final = BookItem.objects.filter(id=borrow.id)
        #     serializer = BookItemSerializer(final, many=True)

        #     context={
        #         "name": "user_name_here",
        #         "success": "its all yours",
        #     }
        #     # return Response(serializer.data,status=status.HTTP_200_OK)
        #     return render(req,'book/borrow.html',context=context)
        # if book_status == 'R' | 'B':
        #     context={
        #         "name": "user_name_here",
        #         "error": "this book has been reserved or taken by someone else. gonna be available in BLABLABLA. book it"
        #     }
        #     # ↑ this msg n' redirect to ↓
        #     return render(req,'book/reservation.html',context=context)
        # else:
        #     context={
        #         "name": "user_name_here",
        #         "error": "try with another book"
        #     }
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        #     return render(req,'book/borrow.html',context=context)
            
        return Response(status=status.HTTP_200_OK)


        



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


