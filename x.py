
class Test(Exception):
    def __init__(self,x) -> None:
        super().__init__()
        self.x = x



def v():
    raise Test(50)


try:
    v()
except Test as e:
    print(e.x)
