from api.models import Book
from django.urls import path
from api.controller.v1.book_controller import BookViewSet

app_label = 'api'
urlpatterns = [
    path('v1/book', BookViewSet.as_view({
                'get': 'list',
                'post': 'create'
            }
        )
    )
]
