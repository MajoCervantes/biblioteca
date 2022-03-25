from django.contrib import admin

from .models import Book, BookItem, Rack


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title',)


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ('book', 'rack', 'price', 'status')
    search_fields = ('barcode', 'rack')


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
