
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.servers.routes import routes

app = FastAPI(routes=routes)


origins = ["http://localhost:8080", ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "main":
    app.run(host="0.0.0.0",port=9000)
