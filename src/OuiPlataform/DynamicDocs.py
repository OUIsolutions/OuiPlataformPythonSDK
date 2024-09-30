
import json
from typing_extensions import List, Union
from requests import post
from .algo import raise_if_its_not_ok
from .BaseSession import BaseSession

class DynamicDoc(BaseSession):

    def __init__(self,url:str,token:str,name:str) -> None:
        super().__init__(url)
        self.token = token
        self.name = name

    def __str__(self) -> str:
        return self.name

    def  get_generator_code(self,output:Union[str,None]=None)->str:
        result = self.autenticated_requisition_json(
            route='/api/dynamic_docs/describe_dynamic_doc',
            headers={'Document':self.name,'Includecode':'true'},
        )
        if output:
            with open(output,'w') as arq:
                arq.write(result['function'])
        return result['function']
