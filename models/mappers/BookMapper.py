from models.Book import Book


class BookMapper:

    @staticmethod
    def map_to_model(entity: dict):
        model = Book()
        model.id = str(entity['_id'])
        model.name = entity['name']
        model.description = entity['description']
        return model

    @staticmethod
    def map_to_entity(model: Book):
        return {'name': model.name, 'description': model.description}
