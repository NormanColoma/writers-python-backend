from bson import ObjectId
from pymongo import MongoClient

from models.mappers.BookMapper import BookMapper

client = MongoClient('localhost', 27017)
db = client.writers
book_collection = db.book


class BookDAO:

    @staticmethod
    def get_books():
        books_found = book_collection.find()
        books = list()
        for book_entity in books_found:
            book = BookMapper.map_to_model(book_entity)
            books.append(book)
        return books

    @staticmethod
    def get_book(book_id):
        book_entity = book_collection.find_one({'_id': ObjectId(book_id)})
        book = BookMapper.map_to_model(book_entity)
        return book

    @staticmethod
    def save_book(book):
        book_entity = BookMapper.map_to_entity(book)
        book_id = book_collection.insert_one(book_entity).inserted_id
        book_entity['_id'] = book_id
        book_created = BookMapper.map_to_model(book_entity)
        return book_created
