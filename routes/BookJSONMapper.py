from typing import Union

from flask import json, Response
from flask.json import JSONEncoder, jsonify, JSONDecoder

from models.Book import Book


class BookMapper(JSONEncoder, JSONDecoder):
    def default(self, o: Book):
        try:
            if isinstance(o, Book):
                return {
                    "id": o.id,
                    "title": o.title,
                    "description": o.description,
                    "coverUrl": o.cover_url,
                    "author_id": o.author_id
                }
        except TypeError:
            pass
        return JSONEncoder.default(self, o)

    def to_object(self, json_obj: dict):
        book = Book()

        book.title = json_obj['title']
        book.description = json_obj['description']
        book.cover_url = json_obj['coverUrl']
        book.author_id = json_obj['author_id']
        return book

    def to_json(self, book: Union[list, Book]):
        if isinstance(book, list):
            return Response(json.dumps(book, cls=BookMapper), mimetype='application/json')
        json_book = self.default(book)
        json_response = jsonify(json_book)
        return json_response
