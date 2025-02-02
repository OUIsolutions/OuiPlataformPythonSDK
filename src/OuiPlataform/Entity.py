import json
from typing import List, Union
from .LoginProps import LoginProps
from .BaseSession import BaseSession

class Entity(BaseSession):

    def __init__(self,url:str,login_props:LoginProps,name:str) -> None:
        super().__init__(url,login_props)

        self.name = name

    def __str__(self) -> str:
        return self.name

    def self_destroy(self):
        self.autenticated_requisition_json(
            route='/api/entity/remove_entity',
            headers={'entity':self.name},
            body=None
        )


    def lock(self):
        self.autenticated_requisition_json(
            route='/api/entity/lock_entity',
            headers={'entity':self.name},
            body=None
        )

    def unlock(self):
        self.autenticated_requisition_json(
            route='/api/entity/unlock_entity',
            headers={'entity':self.name},
            body=None
        )

    def list_all_static_documents(self)->List[str]:
        result =  self.autenticated_requisition_json(
            route='/api/entity/describe_entity',
            headers={'entity':self.name},
            body=None
        )
        docs =list(map(lambda d: d['name'],result['documents']))
        return docs

    def list_jsons(self)->List[str]:
        all = self.list_all_static_documents()
        return list(filter(lambda d:d.endswith('.json'),all))


    def list_all_dynamic_documents(self)->List[str]:
        result =  self.autenticated_requisition_json(
            route='/api/entity/describe_entity',
            headers={'entity':self.name},
            body=None
        )
        docs =list(map(lambda d: d['name'],result['dynamic_docs']))
        return docs



    def get_json(self,name:str,output:Union[str,None]=None)->Union[dict,list]:
        if not name.endswith(".json"):
            name = name + ".json"

        result =  self.autenticated_requisition_json(
            route='/api/entity/get_document',
            headers={'entity':self.name,'document':name},
            body=None
        )
        if output:
            with open(output,"w") as arq:
                arq.write(json.dumps(result,indent=4))
        return result


    def set_json(self,name:str,body:dict):
        if not name.endswith(".json"):
            name = name + ".json"
        self.autenticated_requisition_raw(
            route='/api/entity/add_document',
            headers={'entity':self.name,'document':name},
            body=body
        )

    def get_dynamic_doc(self,name:str,mode:str,output:Union[str,None]=None)->bytes:
        result =  self.autenticated_requisition_bytes(
            route='/api/entity/get_dynamic_document_instance',
            headers={'entity':self.name,'document':name,'mode':mode},
            body=None
        )
        if output:
            with open(output,"wb") as arq:
                arq.write(result)
        return result

    def upload_static_document(self,document_name:str,document:Union[bytes,str]):
        self.autenticated_requisition_raw(
            route='/api/entity/add_document',
            headers={'entity':self.name,'document':document_name},
            body=document
        )


    def upload_static_document_from_file(self,document_name:str,document_file:str):
        with open(document_file,'rb') as arq:
            document = arq.read()

        self.autenticated_requisition_raw(
            route='/api/entity/add_document',
            headers={'entity':self.name,'document':document_name},
            body=document
        )


    def destroy_document(self,name:str):
        self.autenticated_requisition_raw(
            route='/api/entity/remove_document',
            headers={'entity':self.name,'document':name},
        )


    def get_static_doc(self,name:str,output:Union[str,None]=None)->bytes:

        result =  self.autenticated_requisition_bytes(
            route='/api/entity/get_document',
            headers={'entity':self.name,'document':name},
            body=None
        )
        if output:
            with open(output,"wb") as arq:
                arq.write(result)
        return result
