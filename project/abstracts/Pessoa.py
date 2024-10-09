from abc import ABC , abstractmethod
from projeto.models. import Endereco

class Pessoa(ABC):
    def __init__(self,nome:str, telefone :str, email:str,endereco: Endereco):
        self.nome = nome
        self.telefone = telefone
        self.email= email
        self.endereco = endereco
   
    @abstractmethod
    def apresentar(self):
        pass
  