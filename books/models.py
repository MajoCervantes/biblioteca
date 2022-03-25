from uuid import uuid4
from django.db import models
from core.models import LibraryPlace
from .choices import BOOK_FORMAT, BOOK_STATUS, CATEG_CHOICES


# Create your models here.

# class User(django):

# borrowed_books: models.IntegerField(default=0)

#     def __str__(self) -> str:
#         return 'algo'


class Rack(models.Model):
    category = models.CharField(
        max_length=20, choices=CATEG_CHOICES, default='No provided')
    description = models.TextField(default='No desc. provided')

    def __str__(self):
        return self.category


class Book(models.Model):
    author = models.CharField(max_length=50, default='Anon')
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    abstract = models.TextField()
    editorial = models.CharField(max_length=50)
    publication_date = models.DateField(default=None, null=True)
    language = models.CharField(max_length=50)
    number_of_pages = models.IntegerField()
    library = models.ForeignKey(LibraryPlace, on_delete=models.PROTECT, default=None, null=True, blank=True)

    category = models.CharField(
        max_length=20, choices=CATEG_CHOICES, default='No provided')

    def __str__(self):
        return self.title


class BookItem(models.Model):
    barcode = models.UUIDField(default=uuid4)

    book = models.ForeignKey(Book, related_name='bookItem', on_delete=models.PROTECT)

    borrowed_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    book_format = models.CharField(
        max_length=2,
        choices=BOOK_FORMAT,
        default='Format not provided yet',
    )

    rack = models.ForeignKey(Rack, related_name='book',
                             null=True, on_delete=models.SET_NULL)

    status = models.CharField(
        max_length=1,
        choices=BOOK_STATUS,
        default='A'
    )

    def __str__(self):
        return str(self.book) + " | " + str(self.book_format) + " | " + str(self.status)
