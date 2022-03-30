
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import *

router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [

    # 1st
    path("library/", LibraryListGeneric.as_view()),  # √ get n post
    path("library/<int:pk>/", LibraryDetailGeneric.as_view()),  # √ get

    # 2nd
    path("racks/", RackListGeneric.as_view()),  # √ get n post
    path("rack/category/<str:key>/", RackDetailGeneric.as_view()),  # √ get
    path("racks/<int:pk>/", RackDetailGeneric.as_view()),  # √ get

    # 3rd
    # * this for add book and its copies by given num
    path("addbooks/", CreateBookItems.as_view()),  # √ post

    path("books/", BookListGeneric.as_view()),  # √ get n post
    path("books/<int:pk>/", BookDetailGeneric.as_view()),  # √ get



    path("catalog/", Catalog.as_view()),  # √ get

    # *this one is for reserve a book
    path("reservations/", BookReservation.as_view()),   # √ get n post

    # * this one is for borrow a book
    path("borrow/", BorrowBook.as_view()),  # √ get n post

    # * this one is to see all BookItems
    path("bookitems/", BookItemListGeneric.as_view()),  # √ get n post
    path("bookitems/<int:pk>/", BookItemDetailGeneric.as_view()),  # √ get n post

    # TODO borrowed by user
    # path("borrow-by/<str:key>/", .as_view()),



    path("return/", ReturnBook.as_view()),

    path("users/", include(router.urls))
]
