

from src.Session import Session

s = Session("return.oui.tec.br")
s.autenticate('root','root')

e = s.create_entity("gggg")
