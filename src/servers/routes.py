from fastapi.routing import APIRoute
from fastapi import Depends
from src.servers.controllers.todo_controller import TodoController
from src.servers.controllers.user_controller import UserController
from src.auth.jwt_bearer import jwtBearer

def index():
    return {"message": "base route of service"}


TodoController = TodoController()
UserController = UserController()
routes = [
    APIRoute('/', index, methods=["GET"]),
    APIRoute('/todos', TodoController.save_todo, dependencies=[Depends(jwtBearer())], methods=["POST"]),
    APIRoute('/todos', TodoController.get_todos, methods=["GET"]),
    APIRoute('/signup', UserController.save_user, methods=["POST"]),
    APIRoute('/login', UserController.login, methods=["POST"]),

]
