from uuid import uuid4
from django.db import models
from core.models import LibraryPlace
from .choices import BOOK_FORMAT, BOOK_STATUS, SUBJECT_CHOICES


# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=50, default='Anon')
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    number_of_pages = models.IntegerField()
    library = models.ForeignKey(LibraryPlace, on_delete=models.PROTECT)

    # ? auto_now genera la fecha actual en que fue creado el libro
    publication_date = models.DateField(auto_now=True)

    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='education')

    def __str__(self):
        return self.title


class Rack(models.Model):
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='education')

    def __str__(self):
        return self.subject


class BookItem(models.Model):
    # ? uuid4 genera un hash único al momento de ser creado
    barcode = models.UUIDField(primary_key=True, default=uuid4)

    # ? un libro puede tener muchos BookItem, un BookItem pertenece a un libro
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # ? un Rack puede tener muchos BookItem, un BookItem pertenece a un Rack
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)

    is_reference_only = models.BooleanField()
    borrowed_date = models.DateTimeField()
    due_date = models.DateTimeField()

    # ? max_digits es el número total de dígitos que hay en el número especificado.
    # ? Entonces, para un número como 999.99, max_digits sería 5.
    # ? decimal_places(máximo de decimales), 2 por ser una moneda.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # ? Ebook por defecto
    book_format = models.CharField(
        max_length=2,
        choices=BOOK_FORMAT,
        default='EB'
    )
    # ? Available(disponible) por defecto
    status = models.CharField(
        max_length=1,
        choices=BOOK_STATUS,
        default='A'
    )
    date_of_purchase = models.DateTimeField()

    def __str__(self):
        return self.status
