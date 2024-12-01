import json
from requests.adapters import Response
from .ErrorCodes import ErrorCodes
from .LoginProps import LoginProps
from .PlataformError import PlataformError
from requests import post
from typing_extensions import Union

class BaseSession:

    def __init__(self,url:str,login_props:LoginProps) -> None:
        self.url = url
        self.login_props = login_props

    def autenticated_requisition_raw(self,route:str,headers:Union[dict,None]=None,body:Union[dict,list, bytes,str,None,list]=None)->Response:

        if not self.login_props.token:
            creation = post(f'{self.url}/api/public/create_token',headers={
                'login':self.login_props.login,
                'password':self.login_props.password
            })
            parsed = creation.json()
            if creation.status_code < 200 or creation.status_code >= 300:
                raise PlataformError(parsed['code'],parsed['message'])
            self.login_props.token = parsed['token']


        if not headers:
            headers = {}
        headers['token'] = self.login_props.token

        if body.__class__  in [dict,list]:
            body = json.dumps(body,indent=4)
        if body.__class__ == str:
            body =  body.encode("utf-8")

        result = post(f'{self.url}{route}',headers=headers,data=body)
        if result.status_code < 200 or result.status_code >= 300:
            parsed = result.json()
            if parsed['code'] == ErrorCodes.INVALID_TOKEN:
                 self.login_props.token = None
                 self.autenticated_requisition_raw(route,headers,body)
            else:
                 raise PlataformError(parsed['code'],parsed['message'])


        return result

    def autenticated_requisition_json(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None]=None)->dict:
        result = self.autenticated_requisition_raw(route,headers,body)
        result.encoding = 'utf-8'
        return result.json()

    def autenticated_requisition_bytes(self,route:str,headers:Union[dict,None],body:Union[dict, bytes,None]=None)->bytes:
        result = self.autenticated_requisition_raw(route,headers,body)
        return result.content

    def autenticated_requisition_text(self,route:str,headers:dict,body:Union[dict, bytes,None]=None)->str:
        result = self.autenticated_requisition_raw(route,headers,body)
        result.encoding = 'utf-8'
        return result.text
