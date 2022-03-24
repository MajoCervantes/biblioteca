from django.urls import path
from .views import *

urlpatterns = [

    path("library/", LibraryListGeneric.as_view()),
    path("library/<int:pk>/", LibraryDetailGeneric.as_view()),

    # * this for add book and its copies by given num
    path("addbooks/", CreateBookItems.as_view()),
    # * this for add book and its copies by given num

    path("books/", BookListGeneric.as_view()),
    path("books/<str:key>/", BookBy.as_view()),

    path("racks/", RackList.as_view()),
    path("rack/category/<str:key>/", RackByCat.as_view()),
    path("rack/number/<int:key>/", RackByNum.as_view()),

    path("catalog/", Catalog.as_view()),

    path("reserve/", BookReservation.as_view()),

    path("borrow/", BorrowBook.as_view()),

    path("allbooks/", BookItemListGeneric.as_view()),
    path("borrowed/<int:pk>/", BookItemDetailGeneric.as_view()),

    path("borrowby/<str:key>/", BorrowedByUser.as_view()),


]
