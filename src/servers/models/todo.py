
from pydantic import BaseModel, Field, validator

from src.db.Repository import Repository


class Todos(Repository):
    # async def index(self, add):
    #     await add([('', "")])

    def collection(self):
        return 'todos'

    async def saveTodo(self, title: str, description: str):
        
        data = {"title": title,
                "description": description}

        return await self.save(data=data, collection_name=self.collection())

    async def getAll(self, title: str, start: int = 0, limit: int = 0):
        qurey = {}
        if title:
            qurey['title'] = {'$regex': f'.*{title}.*'}
        result = await self.find({
            '$query': qurey,  # filter deleted face
            '$orderby': {
                'updated_at': -1
            }}, self.collection())
        # result.skip(start).limit(limit)
        return result
