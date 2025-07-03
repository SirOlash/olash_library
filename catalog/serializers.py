from rest_framework import serializers


from .models import Book, Author, BookImage


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','first_name', 'last_name', 'email','dob']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    # images = serializers.StringRelatedField(many=True, read_only=True) use this or the one under
    images = serializers.HyperlinkedRelatedField(
        view_name='book-image-detail',
        queryset=BookImage.objects.all(),
        many=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'summary', 'images', 'author' ]

    # author = serializers.RelatedField()

    # author = serializers.ManyRelatedField(
    #     queryset=Author.objects.all(),
    #     read_only=True
    # )
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=255)


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['first_name', 'last_name', 'email']


class AddBookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'summary']


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']
