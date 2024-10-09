from abc import ABC , abstractmethod
from project.models.Endereco import Endereco


class Pessoa(ABC):
    def __init__(self,nome:str, telefone :str, email:str,endereco: Endereco):
        self.nome = nome
        self.telefone = telefone
        self.email= email
        self.endereco = endereco
   
    @abstractmethod
    def salario_final(self):
        pass
  