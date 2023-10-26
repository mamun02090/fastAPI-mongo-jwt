from fastapi import Request, status
from fastapi.responses import JSONResponse
from src.auth.jwt_handler import signJWT
from src.servers.models.user import Users


class UserController:
    def __init__(self) -> None:
        self.user = Users()

    async def save_user(self, request: Request):
        
        request_data = await request.json()
        token = await self.user.saveUser(**request_data)
        
        return JSONResponse(
            status_code=201,
            content={"data": token,
                     "code": status.HTTP_201_CREATED,
                     "message": "successfully save"},
        )
    async def login(self, request: Request):
        request_data = await request.json()
        token = await self.user.loginUser(**request_data)
        
        return JSONResponse(
            status_code=201,
            content={"data": token,
                     "code": status.HTTP_201_CREATED,
                     "message": "successfully logged in"},
        ) 

    
