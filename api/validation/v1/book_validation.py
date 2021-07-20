from api.dto.v1.book_dto import BookDto
from api.models import Book
from rest_framework import serializers

class BookValidation(serializers.Serializer):
    title = serializers.CharField()
    page = serializers.IntegerField()

    def to_dto(self, obj) -> BookDto:
        return BookDto(title=obj.get('title'), page=obj.get('page'))
