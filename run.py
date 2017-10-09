import os

from app.__init__ import create_app

config_name = os.getenv('ENV_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
