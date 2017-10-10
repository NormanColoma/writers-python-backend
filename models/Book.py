class Book:
    __id: str = ""
    __name: str = ""
    __description: str = ""

    def __init__(self):
        pass

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @id.setter
    def id(self, __id: str):
        self.__id = __id

    @name.setter
    def name(self, name: str):
        self.__name = name

    @description.setter
    def description(self, desc: str):
        self.__description = desc
