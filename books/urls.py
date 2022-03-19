from django.urls import path
from .views import BookDetail, BookList, Catalog

urlpatterns = [
    path("books/", BookList.as_view()),
    path("books/<int:pk>/", BookDetail.as_view()),
    path("catalog/", Catalog.as_view())
]
