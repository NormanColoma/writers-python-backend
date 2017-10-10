from abc import abstractmethod

from models import Book


class IBookRepository:
    @abstractmethod
    def get_books(self): raise NotImplementedError

    @abstractmethod
    def get_book(self, book_id: str): raise NotImplementedError

    @abstractmethod
    def save_book(self, book: Book): raise NotImplementedError

    @abstractmethod
    def remove_book(self, book_id: str): raise NotImplementedError
