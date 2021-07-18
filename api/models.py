from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    page = models.IntegerField()

class Author(models.Model):
    name = models.CharField(max_length=255)