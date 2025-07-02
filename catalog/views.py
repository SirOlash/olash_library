from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Book
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
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

def greet(request, name):
    return render(request, 'index.html', {'name': name})


