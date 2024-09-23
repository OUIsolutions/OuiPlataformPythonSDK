from requests import post
from .algo import raise_if_its_not_ok
from .BaseSession import BaseSession

class Entity(BaseSession):

    def __init__(self,name:str) -> None:
        self.name  = name


    def get_json(self,name:str)->dict:
        return self.autenticated_requisition_json('/api/get_document',{'entity':self.name,'document':name})

    def get_dynamic_doc(self,name:str)->bytes:
        pass

    def get_static_doc(self,name:str)->bytes:
