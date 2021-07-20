
from django.db.models.manager import BaseManager
from api.models import Book
from api.dto.v1.book_dto import BookDto

class BookBusiness():
    def create(self, book_dto: BookDto) -> bool:
        book = Book(
            title=book_dto.title,
            page=book_dto.page
        )

        book.save()
        return True

    def update(self, id, book_dto: BookDto) -> bool:
        book = Book.objects.get(pk=id)
        book.title = book_dto.title
        book.page = book_dto.page

        book.save()
        return True

    def delete(self, id) -> BaseManager:
        book = Book.objects.get(pk=id)
        book.delete()
        return True

    def get(self) -> BaseManager:
        return Book.objects.all()

    def get_detail(self, id) -> BaseManager:
        return Book.objects.get(pk=id)

