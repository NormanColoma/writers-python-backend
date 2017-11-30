class Book:
    __id: str
    __title: str
    __description: str
    __coverUrl: str
    __authorId: str
    __created: int
    __updated: int

    def __init__(self):
        pass

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def cover_url(self):
        return self.__coverUrl

    @property
    def author_id(self):
        return self.__authorId

    @property
    def created(self):
        return self.__created

    @property
    def updated(self):
        return self.__updated

    @id.setter
    def id(self, __id: str):
        self.__id = __id

    @title.setter
    def title(self, title: str):
        self.__title = title

    @description.setter
    def description(self, desc: str):
        self.__description = desc

    @cover_url.setter
    def cover_url(self, cover_url: str):
        self.__coverUrl = cover_url

    @author_id.setter
    def author_id(self, author_id: str):
        self.__authorId = author_id

    @created.setter
    def created(self, created: int):
        self.__created = created

    @updated.setter
    def updated(self, updated: int):
        self.__updated = updated
