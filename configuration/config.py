import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mongodb://localhost:27017/'


class ProductionConfig(Config):
    DATABASE_URI = 'mongodb://' + os.getenv('DATABASE') if os.getenv('DATABASE') is not None else 'localhost' + ':27017'


class DevelopmentConfig(Config):
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
