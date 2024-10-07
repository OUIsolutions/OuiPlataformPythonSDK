
from typing import Union


class LoginProps:

    def __init__(self,
        login:Union[str,None] = None,
        password:Union[str,None]=None,
        token:Union[str,None]=None) -> None:

        if not token:
            if not login:
                raise Exception("login must be provided")
            if not password:
               raise Exception("password must be provided")

        self.login = login
        self.password = password
        self.token = token
