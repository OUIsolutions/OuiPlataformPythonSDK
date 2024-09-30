
import json
from typing_extensions import List, Union
from requests import post
from .algo import raise_if_its_not_ok
from .BaseSession import BaseSession

class Search(BaseSession):

    def __init__(self,url:str,token:str,name:str) -> None:
        super().__init__(url)
        self.token = token
        self.name = name

    def __str__(self) -> str:
        return self.name

    def  get_search_code(self,output:Union[str,None]=None)->str:
        result = self.autenticated_requisition_json(
            route='/api/search/get_search_props',
            headers={'Search':self.name,'Includecode':'true'},
        )
        if output:
            with open(output,'w') as arq:
                arq.write(result['function'])
        return result['function']

    def get_search_props(self)->dict:
        result = self.autenticated_requisition_json(
            route='/api/search/get_search_props',
            headers={'Search':self.name,'includeprops':'true'},
        )
        return result['props']

    def set_search_code(self,code:str):
        self.autenticated_requisition_raw(
            route='/api/search/set_search_code',
            headers={'Search':self.name},
            body=code
        )

    def set_search_props(self,props:dict):
        self.autenticated_requisition_raw(
            route='/api/search/set_search_props',
            headers={'Search':self.name},
            body=props
        )
