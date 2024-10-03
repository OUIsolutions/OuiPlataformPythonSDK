
from typing_extensions import  Union
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
            headers={'Document':self.name,'Include-Generator-Code':'true'},
        )
        if output:
            with open(output,'w') as arq:
                arq.write(result['generator_function'])
        return result['generator_function']


    def  get_validator_code(self,output:Union[str,None]=None)->str:
        result = self.autenticated_requisition_json(
            route='/api/dynamic_docs/describe_dynamic_doc',
            headers={'Document':self.name,'Include-Validator-Code':'true'},
        )
        if output:
            with open(output,'w') as arq:
                arq.write(result['validator_function'])
        return result['validator_function']


    def set_validator_code(self,code:str):
        self.autenticated_requisition_raw(
            route='/api/dynamic_docs/set_dynamic_doc_validator_code',
            headers={'Document':self.name},
            body=code
        )


    def set_generator_code(self,code:str):
            self.autenticated_requisition_raw(
                route='/api/dynamic_docs/set_dynamic_doc_generator_code',
                headers={'Document':self.name},
                body=code
            )
