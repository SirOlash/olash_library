from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_books),

    path("authors/", views.AddAuthorView.as_view(), name="add_author"),

    path("authors/<int:pk>/", views.GetUpdateDeleteAuthorView.as_view(), name="get_author_detail"),

    path("authors/update/<int:pk>/", views.update_author, name="update_author"),

    path("authors/delete/<int:pk>/", views.update_author, name="delete_author"),

    path("get/authors/", views.get_authors , name="get_authors"),

    path("greet/<name>", views.greet)

]
