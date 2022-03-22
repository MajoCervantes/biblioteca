from django.contrib import admin

from .models import Book, BookItem, Rack

# Register your models here.
admin.site.register(Rack)
admin.site.register(BookItem)
# admin.site.register(Book)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title',)
