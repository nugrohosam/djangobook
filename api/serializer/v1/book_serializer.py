from api.models import Book
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    page = serializers.IntegerField()
