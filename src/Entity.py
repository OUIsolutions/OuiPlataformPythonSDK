from requests import post
from .algo import raise_if_its_not_ok
from .BaseSession import BaseSession

class Entity(BaseSession):

    def __init__(self,url:str,token:str,name:str) -> None:
        super().__init__(url)
        self.token = token
        self.name = name



    def get_json(self,name:str)->dict:
        return self.autenticated_requisition_json(
            route='/api/entity/get_document',
            headers={'entity':self.name,'document':name},
            body=None
        )

    def set_json(self,name:str,body:dict):
        self.autenticated_requisition_raw(
            route='/api/entity/add_document',
            headers={'entity':self.name,'document':name},
            body=body
        )

    def get_dynamic_doc(self,name:str)->bytes:
        return self.autenticated_requisition_bytes(
            route='/api/entity/get_dynamic_document_instance',
            headers={'entity':self.name,'document':name},
            body=None
        )

    def get_static_doc(self,name:str)->bytes:
        return self.autenticated_requisition_bytes(
            route='/api/entity/get_document',
            headers={'entity':self.name,'document':name},
            body=None
        )
