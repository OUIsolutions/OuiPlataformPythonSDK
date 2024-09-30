from typing import List
from typing_extensions import Union
from .Entity import Entity
from .algo import raise_if_its_not_ok
from .BaseSession import BaseSession
from requests import post


class Session(BaseSession):

    def __init__(self,url:str,):
        super().__init__(url)

    def autenticate(self,login:str,password:str):
        result = post(f'{self.url}/api/public/create_token',headers={'login':login,'password':password})
        raise_if_its_not_ok(result)
        self.token = result.json()['token']

    def get_entity(self,name:str)->Entity:
        return Entity(self.url,self.token,name)

    def list_entities(self,
        contains:Union[str,None]=None,
        quantity:Union[int,None]=None,
        created_before:Union[str,None]=None,
        created_after:Union[str,None]=None,
        search:Union[str,None]=None,
        search_props:Union[dict,None]=None)->List[Entity]:

        headers = {
            'Contains':contains,
            'Quantity':quantity,
            'Created-After':created_after,
            'Created-Before':created_before,
            'Search':search
        }
        result = self.autenticated_requisition_json(
            route='/api/entity/list_entities',
            headers=headers,
            body=search_props
        )

        entities = []
        for  e in result:
            if e.get('name'):
               entities.append(Entity(self.url,self.token,e['name']))
            if e.get('Hide.name'):
                  entities.append(Entity(self.url,self.token,e['Hide.name']))
        return entities




    def create_entity(self,name:str)->Entity:
        self.autenticated_requisition_raw(route='/api/entity/add_entity',headers={'Entity':name},body=None)
        return Entity(self.url,self.token,name)
