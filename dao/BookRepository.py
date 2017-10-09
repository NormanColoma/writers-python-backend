from abc import abstractmethod


class BookRepository:
    @abstractmethod
    def get_books(self): raise NotImplementedError

    @abstractmethod
    def get_book(self, book_id): raise NotImplementedError

    @abstractmethod
    def save_book(self, book): raise NotImplementedError