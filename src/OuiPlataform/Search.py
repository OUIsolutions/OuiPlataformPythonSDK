
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
