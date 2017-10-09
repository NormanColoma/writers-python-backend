from flask import Flask, g
from pymongo import MongoClient

from config.config import app_config
from routes.books import books_api


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    def connect_db():
        return MongoClient(app.config['DATABASE_URI'])

    def get_db():
        with app.app_context():
            db = getattr(g, 'mono_db', None)
            if db is None:
                db = g.mono_db = connect_db()
            return db

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'mono_db'):
            g.mono_db.close()

    app.config['db'] = get_db()
    app.register_blueprint(books_api)
    return app
