
import json
from typing_extensions import List, Union
from requests import post
from .algo import raise_if_its_not_ok
from .BaseSession import BaseSession

class Mapper(BaseSession):

    def __init__(self,url:str,token:str,name:str) -> None:
        super().__init__(url)
        self.token = token
        self.name = name

    def __str__(self) -> str:
        return self.name


    def  get_mapper_function(self,output:Union[str,None]=None)->str:
        result = self.autenticated_requisition_json(
            route='/api/dynamic_docs/describe_dynamic_doc',
            headers={'Document':self.name,'Include-Generator-Code':'true'},
        )
        if output:
            with open(output,'w') as arq:
                arq.write(result['generator_function'])
        return result['generator_function']

    def set_mapper_function(self,code:str):
            self.autenticated_requisition_raw(
                route='/api/dynamic_docs/set_dynamic_doc_generator_code',
                headers={'Document':self.name},
                body=code
            )
