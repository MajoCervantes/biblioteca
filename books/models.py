from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.CharField(max_length=50, default='Anon')
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

    ISBN = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    subject = models.TextField()
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.title


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    barcode = models.CharField(max_length=50)
    is_reference_only = models.BooleanField()
    borrowed = models.DateTimeField()
    due_date = models.DateTimeField()
    price = models.IntegerField()
    # format = models.
    # status = models.
    date_of_purchase = models.DateTimeField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.status
