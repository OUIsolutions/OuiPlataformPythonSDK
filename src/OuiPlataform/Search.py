
from typing import Union

from .LoginProps import LoginProps
from .BaseSession import BaseSession

class Search(BaseSession):

    def __init__(self,url:str,login_props:LoginProps,name:str) -> None:
        super().__init__(url,login_props)
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

    def remove(self):
        self.autenticated_requisition_raw(
            route='/api/search/remove_search',
            headers={'Search':self.name}
        )

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

    def set_search_props(self,props:list):
        self.autenticated_requisition_raw(
            route='/api/search/set_search_props',
            headers={'Search':self.name},
            body=props
        )
