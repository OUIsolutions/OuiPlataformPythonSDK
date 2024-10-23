from .BaseSession import BaseSession
from .LoginProps import LoginProps

class LuaError(BaseSession):

    def __init__(self,url:str,login_props:LoginProps, name:str,entity:str,id:str,content:str,creation_unix:int,creation:str) -> None:
        super().__init__(url,login_props)
        self.name = name
        self.entity =entity
        self.id = id
        self.content = content
        self.creation_unix = creation_unix
        self.creation = creation

    def self_destroy(self):
        self.autenticated_requisition_raw(
            '/api/lua_errors/destroy_lua_errors',
            body=[self.id]
        )

    def __str__(self) -> str:
        return self.id
