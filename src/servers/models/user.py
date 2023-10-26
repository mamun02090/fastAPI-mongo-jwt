
from pydantic import EmailStr, BaseModel, Field, validator
from src.auth.jwt_handler import signJWT, decodeJWT
from src.db.Repository import Repository
from fastapi import HTTPException

class Users(Repository):
    # async def index(self, add):
    #     await add([('', "")])

    def collection(self):
        return 'users'

    async def saveUser(self, name: str, email: EmailStr, password: str):
        data = {"name": name,
                "email": email,
                "password": password}
        user = await self.getUser(email)
        print(user)
        if(user):
            raise HTTPException(status_code=500, detail ="User Already Exists. Login instead")
        user = await self.save(data=data, collection_name=self.collection())
        if(user):
            return signJWT(email)
        else:
            return []
    
    async def loginUser(self, email: EmailStr, password: str):
        user = await self.getUser(email)
        print(user)
        if(user):
            if(user[0]["password"] == password):
                return signJWT(email)
            else:
                raise HTTPException(status_code=403, detail= "Invalid password or Email")
        else: raise HTTPException(status_code=403, detail= "Invalid password or Email")
        
        

    async def getUser(self, email: EmailStr):
        result = await self.find({"email": email}, self.collection())
        return result
