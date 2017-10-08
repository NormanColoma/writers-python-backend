from flask import json, Response
from flask.json import JSONEncoder, jsonify, JSONDecoder

from models.Book import Book


class BookMapper(JSONEncoder, JSONDecoder):
    def default(self, o):
        try:
            if isinstance(o, Book):
                return {"id": o.id, "name": o.name, "description": o.description}
        except TypeError:
            pass
        return JSONEncoder.default(self, o)

    def to_object(self, json_obj):
        book = Book()

        book.name = json_obj['name']
        book.description = json_obj['description']
        return book

    def to_json(self, book):
        if isinstance(book, list):
            return Response(json.dumps(book, cls=BookMapper), mimetype='application/json')
        json_book = self.default(book)
        json_response = jsonify(json_book)
        return json_response
