from api.response.v1.book_response import BookResponse
from api.business.book_business import BookBusiness
from api.dto.v1.book_dto import BookDto
from utils.parser.validation import ValidateAndSetDto
from utils.parser.json import json_to_data, response_data, response_items, response_success
from api.validation.v1.book_validation import BookValidation
from rest_framework.views import APIView
from django.http import HttpResponse
from api.models import Book


class BookController(APIView):
    book_business = BookBusiness()

    def get(self, request, format=None):
        books = self.book_business.get()
        books_response = [BookResponse(id=book.id, title=book.title, page=book.page).to_json() for book in books]
        return response_items(items=books_response)

    def post(self, request, format=None):
        data = json_to_data(request.body)
        validated_data = ValidateAndSetDto[BookValidation, BookDto]()
        book_dto = validated_data.validate_and_get_dto(serializer=BookValidation(data=data))
        self.book_business.create(book_dto)
        return response_success(message='success create')


class BookByIdController(APIView):
    book_business = BookBusiness()
    
    def get(self, request, id, format=None):
        book = self.book_business.get_detail(id=id)
        book_response = BookResponse(id=book.id, title=book.title, page=book.page).to_json()
        return response_data(data=book_response)

    def put(self, request, id, format=None):
        data = json_to_data(request.body)
        validated_data = ValidateAndSetDto[BookValidation, BookDto]()
        book_dto = validated_data.validate_and_get_dto(serializer=BookValidation(data=data))
        self.book_business.update(id=id, book_dto=book_dto)
        return response_success(message='success delete')

    def delete(self, request, id, format=None):
        self.book_business.delete(id=id)
        return response_success(message='success update')
