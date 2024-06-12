from .app import create_app
from .db import init_db


if __name__ == "__main__":
    app = create_app()
    app.run()

def init_db():
    create_app()
    init_db()