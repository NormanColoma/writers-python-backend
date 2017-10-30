from models.Book import Book


class BookMapper:

    @staticmethod
    def map_to_model(entity: dict):
        model = Book()
        model.id = str(entity['_id'])
        model.title = entity['title']
        model.description = entity['description']
        model.cover_url = entity['coverUrl']
        model.author_id = entity['author_id']
        return model

    @staticmethod
    def map_to_entity(model: Book):
        return {
            'title': model.title,
            'description': model.description,
            'coverUrl': model.cover_url,
            'author_id': model.author_id
        }
