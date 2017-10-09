import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mongodb://localhost:27017/'


class ProductionConfig(Config):
    DATABASE_URI = 'mongodb://' + os.getenv('DATABASE') + ':27017'


class DevelopmentConfig(Config):
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
