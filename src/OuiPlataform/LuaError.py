
class LuaError:

    def __init__(self,name:str,entity:str,id:str,content:str,creation_unix:int,creation:str) -> None:
        self.name = name
        self.entity =entity
        self.id = id
        self.content = content
        self.creation_unix = creation_unix
        self.creation = creation

    def __str__(self) -> str:
        return self.id
