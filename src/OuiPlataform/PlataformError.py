
class PlataformError (Exception):

    def __init__(self,code:int,message:str) -> None:
        super().__init__()
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return self.message
