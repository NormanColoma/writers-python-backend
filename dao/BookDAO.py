from bson import ObjectId
from flask import current_app

from dao.IBookRepository import IBookRepository
from models import Book
from models.mappers.BookMapper import BookMapper


class BookDAO(IBookRepository):
    def __init__(self):
        self.config = current_app.config.get('db')
        self.book_collection = self.config.writers.book

    def get_books(self):
        books_found = self.book_collection.find()
        books = list()
        for book_entity in books_found:
            book = BookMapper.map_to_model(book_entity)
            books.append(book)
        return books

    def get_book(self, book_id: str):
        book_entity = self.book_collection.find_one({'_id': ObjectId(book_id)})
        book = BookMapper.map_to_model(book_entity)
        return book

    def save_book(self, book: Book):
        book_entity = BookMapper.map_to_entity(book)
        book_id = self.book_collection.insert_one(book_entity).inserted_id
        book_entity['_id'] = book_id
        book_created = BookMapper.map_to_model(book_entity)
        return book_created

    def remove_book(self, book_id: str):
        self.book_collection.delete_one({'_id': ObjectId(book_id)})
        return None

