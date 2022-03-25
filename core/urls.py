from django.urls import path, include

urlpatterns = [
    path("api/", include("books.urls")),
    # ? Agregar botón para hacer login desde rest_framework
    path("api/login", include("rest_framework.urls"))
]
