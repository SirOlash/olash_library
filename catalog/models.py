import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from user.models import Author


# Create your models here.

class Genre(models.Model):
    GENRE_CHOICES = (
        ("R", "ROMANCE"),
        ("C", "COMEDY"),
        ("P", "POLITICS"),
        ("F", "FINANCE")
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="F", unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    LANGUAGE_CHOICES = (
        ("En", "ENGLISH"),
        ("Yo", "YORUBA"),
        ("FR", "French"),
        ("IG", "IGBO"),
    )
    name = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="En")
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=11)
    dob = models.DateField(blank=False, null=False)
    dod = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    isbn = models.CharField(max_length=11, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, related_name="books")


    def __str__(self):
        return self.title

class BookImage(models.Model):
    # title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="book/images", blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class BookInstance(models.Model):
    LOAN_STATUS = (
        ("A", "AVAILABLE"),
        ("B", "BORROWED"),
        ("M", "MAINTENANCE"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default="A")
    return_date = models.DateTimeField(blank=False, null=False)
    comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class BookImage(models.Model):
        image = models.ImageField(upload_to="book/images", blank=True)
        book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")


        def __str__(self):
            return self.image.url


