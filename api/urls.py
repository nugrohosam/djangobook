from api.models import Book
from django.urls import path
from api.controller.v1.book_controller import BookController, BookByIdController

app_label = 'api'
urlpatterns = [
    path('v1/book', BookController.as_view()),
    path('v1/book/<int:id>', BookByIdController.as_view())
]
