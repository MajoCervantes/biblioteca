from django.urls import path
from .views import BookDetailGeneric, BookItemDetailGeneric, BookItemListGeneric, BookListGeneric, Catalog, LibraryDetailGeneric, LibraryListGeneric, RackByCat, RackByNum, RackList  # noqa E501

urlpatterns = [

    path("library/", LibraryListGeneric.as_view()),
    path("library/<int:pk>/", LibraryDetailGeneric.as_view()),

    path("books/", BookListGeneric.as_view()),
    path("books/<int:pk>/", BookDetailGeneric.as_view()),

    path("racks/", RackList.as_view()),
    path("rack/category/<str:key>/", RackByCat.as_view()),
    path("rack/number/<int:key>/", RackByNum.as_view()),

    path("booksitem/", BookItemListGeneric.as_view()),
    path("booksitem/<int:pk>/", BookItemDetailGeneric.as_view()),

    path("catalog/", Catalog.as_view())
]
