
from api.repositories.book_repository import BookRepository
from django.db.models.manager import BaseManager
from api.models import Book
from api.dto.v1.book_dto import BookDto

class BookBusiness():
    book_repository = BookRepository()

    def create(self, book_dto: BookDto) -> bool:
        self.book_repository.create(book_dto=book_dto)
        return True

    def update(self, id, book_dto: BookDto) -> bool:
        self.book_repository.update(id=id, book_dto=book_dto)
        return True

    def delete(self, id) -> BaseManager:
        self.book_repository.delete(id=id)
        return True

    def get(self) -> BaseManager:
        return Book.objects.all()

    def get_detail(self, id) -> BaseManager:
        return Book.objects.get(pk=id)

