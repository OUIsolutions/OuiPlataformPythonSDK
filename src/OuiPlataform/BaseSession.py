import json
from requests.adapters import Response
from .PlataformError import PlataformError
from requests import post
from typing_extensions import Union

class BaseSession:

    def __init__(self,url:str) -> None:
        self.url = url
        self.token = None

    def autenticated_requisition_raw(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,str,None,list]=None)->Response:
        if not headers:
            headers = {}
        headers['token'] = self.token
        if body.__class__  in [dict,list]:
            body = json.dumps(body,indent=4)
        if body.__class__ == str:
            body =  body.encode("utf-8")

        result = post(f'{self.url}{route}',headers=headers,data=body)
        if result.status_code < 200 or result.status_code >= 300:
            parsed = result.json()
            raise PlataformError(parsed['code'],parsed['message'])


        return result

    def autenticated_requisition_json(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None]=None)->dict:
        result = self.autenticated_requisition_raw(route,headers,body)
        return result.json()

    def autenticated_requisition_bytes(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None]=None)->bytes:
        result = self.autenticated_requisition_raw(route,headers,body)
        return result.content

    def autenticated_requisition_text(self,route:str,headers:dict,body:Union[dict, bytes,None]=None)->str:
        result = self.autenticated_requisition_raw(route,headers,body)
        return result.text
