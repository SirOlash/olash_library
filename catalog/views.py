from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from . import serializers
from .models import Book, Author, BookImage
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer, BookImageSerializer


# Create your views here.

@api_view()
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # return HttpResponse("Hello, world. You're at the books page.")
@api_view(["POST"])
def add_author(request):
    author = AuthorSerializer(data=request.data)
    author.is_valid(raise_exception=True)
    author.save()
    return Response(author.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT", "PATCH"])
def update_author(request, pk):
    author = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(author, data=request.data)
    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    # return Response(serializer.data, status=status.HTTP_200_OK) Similar to what is under
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_author(request, pk):
    author = Author.objects.get(pk=pk)
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



class GetUpdatedAuthorView(UpdateAPIView):
    queryset = Author.objects.all()


def greet(request, name):
    return render(request, 'index.html', {'name': name})

# @api_view(["GET"])
# def image_detail(request, pk):
#     book_image = BookImage.objects.get(pk=pk)
#     serializer = BookImageSerializer(book_image)
#     return Response(serializer.data)

class AddAuthorView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return BookSerializer
        elif self.request.method == 'POST':
            return AuthorSerializer

        return BookSerializer

@api_view(['GET'])
def image_detail(request, pk):
    book_image = get_object_or_404(BookImage, pk=pk)
    serializer = BookImageSerializer(book_image)
    return Response(serializer.data, status=status.HTTP_200_OK)

class BookImageViewSet(viewsets.ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer

