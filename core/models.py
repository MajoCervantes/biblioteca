from django.db import models


# Create your models here.
class LibraryPlace(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}({self.address})'
