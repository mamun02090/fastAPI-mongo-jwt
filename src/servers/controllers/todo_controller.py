from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.servers.models.todo import Todos


class TodoController:
    def __init__(self) -> None:
        self.todos = Todos()

    async def save_todo(self, request: Request):
        request_data = await request.json()
        await self.todos.saveTodo(**request_data)

        return JSONResponse(
            status_code=201,
            content={"data": None,
                     "code": status.HTTP_201_CREATED,
                     "message": "successfully save"},
        )

    async def get_todos(self, title: str = None):
        return await self.todos.getAll(title)
