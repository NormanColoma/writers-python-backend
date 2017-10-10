from flask import Blueprint, request, Response

from dao.BookDAO import BookDAO
from routes.BookJSONMapper import BookMapper

books_api = Blueprint('books', __name__)


@books_api.route("/books")
def get_books():
    dao = BookDAO()
    books = dao.get_books()
    json_mapper = BookMapper()
    response = json_mapper.to_json(books)
    return response


@books_api.route('/books/<book_id>')
def search_book(book_id: str):
    dao = BookDAO()
    book = dao.get_book(book_id)
    json_mapper = BookMapper()
    response = json_mapper.to_json(book)
    return response


@books_api.route('/books/new', methods=['POST'])
def add_book():
    json_mapper = BookMapper()
    book = json_mapper.to_object(request.get_json())
    dao = BookDAO()
    created_book = dao.save_book(book)
    response = json_mapper.to_json(created_book)
    response.status_code = 201
    return response


@books_api.route('/books/<book_id>', methods=['DELETE'])
def remove_book(book_id: str):
    dao = BookDAO()
    dao.remove_book(book_id)
    return Response(status=204)
