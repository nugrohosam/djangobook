from api.response.v1.book_response import BookResponse
from api.business.book_business import BookBusiness
from api.dto.v1.book_dto import BookDto
from utils.parser.validation import ValidateAndSetDto
from utils.parser.json import json_to_data, reponse_data, response_items, reponse_success
from api.validation.v1.book_validation import BookValidation
from rest_framework.views import APIView
from django.http import HttpResponse
from api.models import Book


class BookController(APIView):
    book_business = BookBusiness()

    def get(self, request, format=None):
        books = self.book_business.get()
        books_response = [BookResponse(title=book.title, page=book.page).to_json() for book in books]
        return response_items(books_response)

    def post(self, request, format=None):
        data = json_to_data(request.body)
        validated_data = ValidateAndSetDto[BookValidation, BookDto]()
        book_dto = validated_data.validate_and_get_dto(serializer=BookValidation(data=data))

        self.book_business.create(book_dto)
        return reponse_success('success create')


class BookByIdController(APIView):
    def get(self, request, id, format=None):
        return HttpResponse("detail")

    def put(self, request, id, format=None):
        return HttpResponse("update")

    def delete(self, request, id, format=None):
        return HttpResponse("delete")
