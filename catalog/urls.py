from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_books),
    path("authors/", views.add_author, name="add_author"),

    path("greet/<name>", views.greet)
]
