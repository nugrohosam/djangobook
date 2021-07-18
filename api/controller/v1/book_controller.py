from api.response.v1.book_response import BookResponse
from rest_framework.response import Response
from api.permissions.role_permission import RolePermission
from api.models import Book
from rest_framework import status, viewsets
from api.serializer.v1.book_serializer import BookSerializer
from rest_framework.decorators import permission_classes

@permission_classes([RolePermission])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
