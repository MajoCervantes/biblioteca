from django.urls import path
from .views import *

urlpatterns = [

    path("library/", LibraryListGeneric.as_view()),
    path("library/<int:pk>/", LibraryDetailGeneric.as_view()),

    # * this for add book and its copies by given num
    path("addbooks/", CreateBookItems.as_view()),

    path("books/", BookListGeneric.as_view()),
    path("books/<str:key>/", BookBy.as_view()),

    path("racks/", RackList.as_view()),
    path("rack/category/<str:key>/", RackByCat.as_view()),
    path("rack/number/<int:key>/", RackByNum.as_view()),

    path("catalog/", Catalog.as_view()),


    # TODO reserve a book
    path("reserve/", BookReservation.as_view()),

    # * this one is for borrow a book
    path("borrow/", BorrowBook.as_view()),

    # * this one is to see all BookItems
    path("allbooks/", BookItemListGeneric.as_view()),
    path("borrowed/<int:pk>/", BookItemDetailGeneric.as_view()),

    # TODO borrowed by user
    # path("borrowby/<str:key>/", .as_view()),

    # TODO return a book
    # path("return/", .as_view()),


]
