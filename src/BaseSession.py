from requests.adapters import Response
from .algo import raise_if_its_not_ok

from requests import post
from typing_extensions import Union

class BaseSession:

    def __init__(self,url:str) -> None:
        self.url = url
        self.token = None

    def autenticated_requisition_raw(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None])->Response:
        if not headers:
            headers = {}
        headers['token'] = self.token

        result = post(f'{self.url}/{route}',headers=headers,data=body)
        raise_if_its_not_ok(result)
        return result

    def autenticated_requisition_json(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None])->dict:
        result = self.autenticated_requisition_raw(route,headers,body)
        return result.json()

    def autenticated_requisition_bytes(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None])->bytes:
        result = self.autenticated_requisition_raw(route,headers,body)
        return result.content

    def autenticated_requisition_text(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None])->str:
        result = self.autenticated_requisition_raw(route,headers,body)
        return result.text
