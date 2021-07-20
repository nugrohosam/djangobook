from django.db.models.manager import BaseManager
from api.models import Book
from api.dto.v1.book_dto import BookDto


class BookRepository():
    def create(self, book_dto: BookDto):
        book = Book(
            title=book_dto.title,
            page=book_dto.page
        )

        book.save()

    def update(self, id, book_dto: BookDto):
        book = Book.objects.get(pk=id)
        book.title = book_dto.title
        book.page = book_dto.page

        book.save()

    def delete(self, id):
        book = Book.objects.get(pk=id)
        book.delete()

class BookQueryRepository():
    def get(self) -> BaseManager:
        return Book.objects.all()

    def detail(self, id):
        return Book.objects.get(pk=id)
