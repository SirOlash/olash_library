from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')

router.register('images', BookImageViewSet, basename='book-images')

# print(router.urls)

urlpatterns = [

    path('', include(router.urls)),

    # path("", views.get_books),

    path("authors/", views.AddAuthorView.as_view(), name="add_author"),

    path("authors/<int:pk>/", views.GetUpdateDeleteAuthorView.as_view()),

    # path("authors/update/<int:pk>/", views.update_author, name="update_author"),

    # path("authors/delete/<int:pk>/", views.update_author, name="delete_author"),

    # path("get/authors/", views.get_authors , name="get_authors"),

    # path("greet/<name>", views.greet),

    # path("Images/<int:pk>/", views.image_detail, name="book-image-detail"),

]
