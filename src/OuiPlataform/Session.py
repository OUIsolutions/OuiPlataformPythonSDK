from .Entity import Entity
from .algo import raise_if_its_not_ok
from .BaseSession import BaseSession
from requests import post


class Session(BaseSession):

    def __init__(self,url:str,):
        super().__init__(url)

    def autenticate(self,login:str,password:str):
        result = post(f'https://{self.url}/api/public/create_token',headers={'login':login,'password':password})
        raise_if_its_not_ok(result)
        self.token = result.json()['token']

    def get_entity(self,name:str)->Entity:
        return Entity(self.url,self.token,name)

    def create_entity(self,name:str)->Entity:
        self.autenticated_requisition_raw(route='/api/entity/add_entity',headers={'Entity':name},body=None)
        return Entity(self.url,self.token,name)
