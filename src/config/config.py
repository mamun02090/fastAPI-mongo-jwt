from src.config.database import db


def config():
    return dict(
        **db()
    )
