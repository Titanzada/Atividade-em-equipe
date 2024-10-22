from abc import ABC , abstractmethod
from project.models.Endereco import Endereco


class Pessoa(ABC):
    def __init__(self,nome:str, telefone :str, email:str,endereco: Endereco, salario:float):
        self.nome = nome
        self.telefone = telefone
        self.email= email
        self.endereco = endereco
        self.salario = self.salario_final
   
    @abstractmethod
    def salario_final(salario):
        pass
  