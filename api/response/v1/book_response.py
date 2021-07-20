from array import array
import json
from json.encoder import JSONEncoder
from api.models import Book


class BookResponse():
    def __init__(self, title, page):
        self.title = title
        self.page = page

    def to_json(self):
        return self.__dict__
