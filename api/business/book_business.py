
from django.db.models.manager import BaseManager
from api.models import Book
from api.dto.v1.book_dto import BookDto

class BookBusiness():
    def create(self, bookDto: BookDto) -> bool:
        book = Book(
            title=bookDto.title,
            page=bookDto.page
        )

        book.save()
        return True

    def get(self) -> BaseManager:
        return Book.objects.all()

