from typing import List
from typing import Union

from .LuaError import LuaError
from .LoginProps import LoginProps
from .Entity import Entity
from .BaseSession import BaseSession
from .Search import Search
from .DynamicDocs import DynamicDoc
from requests import post


class Session(BaseSession):

    def __init__(self,url:str,login:Union[str,None],password:Union[str,None],token:Union[str,None]=None):
        super().__init__(url,LoginProps(login,password,token))

    def get_entity(self,name:str)->Entity:
        return Entity(self.url,self.login_props,name)

    def list_searchs(
        self,
        contains:Union[str,None]=None,
        quantity:Union[int,None]=None,
        created_before:Union[str,None]=None,
        created_after:Union[str,None]=None
    )->List[Search]:
        headers = {
            'Contains':contains,
            'Quantity':quantity,
            'Created-After':created_after,
            'Created-Before':created_before
        }
        result = self.autenticated_requisition_json(
            route='/api/search/list_search',
            headers=headers
        )
        return list(map(lambda s:Search(self.url,self.login_props,s['name']),result))



    def list_dynamic_docs(
      self,
      contains:Union[str,None]=None,
      quantity:Union[int,None]=None,
      created_before:Union[str,None]=None,
      created_after:Union[str,None]=None
  )->List[DynamicDoc]:
      headers = {
          'Contains':contains,
          'Quantity':quantity,
          'Created-After':created_after,
          'Created-Before':created_before
      }
      result = self.autenticated_requisition_json(
          route='/api/dynamic_docs/list_documents',
          headers=headers
      )
      return list(map(lambda s:DynamicDoc(self.url,self.login_props,s['name']),result))


    def get_search(self,name)->Search:
        return Search(self.url,self.login_props,name)


    def create_search(self,name)->Search:
        self.autenticated_requisition_raw(
            route='/api/search/add_search',
            headers={'Search':name}
        )
        return Search(self.url,self.login_props,name)

    def list_entities(self,
        contains:Union[str,None]=None,
        chunk:int=1,
        quantity:int=30,
        created_before:Union[str,None]=None,
        created_after:Union[str,None]=None,
        search:Union[str,None]=None,
        search_props:Union[dict,None]=None)->List[Entity]:

        headers = {
            'Contains':contains,
            'Quantity':str(quantity),
            'Chunk':str(chunk),
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
               entities.append(Entity(self.url,self.login_props,e['name']))
            if e.get('Hide.name'):
                  entities.append(Entity(self.url,self.login_props,e['Hide.name']))
        return entities

    def list_lua_errors(self,
        chunk:int=1,
        quantity:int=30,
        error_name:Union[str,None]=None,
        entity:Union[str,None]=None,
        created_before:Union[str,None]=None,
        created_after:Union[str,None]=None

        )->List[LuaError]:

        headers = {
            'Quantity':str(quantity),
            'Chunk':str(chunk),
            'errorname':error_name,
            'entity':entity,
            'Created-After':created_after,
            'Created-Before':created_before
        }

        result = self.autenticated_requisition_json(
            route='/api/lua_errors/list_lua_errors',
            headers=headers
        )
        errors = []
        for e in result:
            created = LuaError(
                url=self.url,
                login_props=self.login_props,
                name=e['error_name'],
                entity=e.get('entity_name'),
                id=e['id'],
                content=e['content'],
                creation_unix=e['creation_unix'],
                creation=e['creation']
            )
            errors.append(created)
        return errors

    def create_entity(self,name:str)->Entity:
        self.autenticated_requisition_raw(route='/api/entity/add_entity',headers={'Entity':name},body=None)
        return Entity(self.url,self.login_props,name)
