from flask import Flask, request

from BookJSONMapper import BookMapper
from dao.BookDAO import BookDAO

app = Flask(__name__)
json_mapper = BookMapper()


@app.route('/books')
def get_books():
    books = BookDAO.get_books()
    response = json_mapper.to_json(books)
    return response


@app.route('/books/<book_id>')
def search_book(book_id):
    book = BookDAO.get_book(book_id)
    response = json_mapper.to_json(book)
    return response


@app.route('/books/new', methods=['POST'])
def add_book():
    book = json_mapper.to_object(request.get_json())
    created_book = BookDAO.save_book(book)
    response = json_mapper.to_json(created_book)
    response.status_code = 201
    return response


if __name__ == '__main__':
    app.run()
