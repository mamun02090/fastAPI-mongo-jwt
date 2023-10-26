from dotenv import load_dotenv
from src.helpers.env import env

load_dotenv()

def db() -> dict:
    return {
        "db": {
            "url": env("MONGO_URL", "mongodb://localhost:27017/"),
            "name":  env("DATABASE_NAME", "database_name"),
            "user": env("USERNAME", ""),
            "password": env("PASSWORD", "")
        }
    }
