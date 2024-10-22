
from project.abstracts.Pessoa import Pessoa
from project.models.Endereco import Endereco


class motoboy(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float):
        super().__init__(nome, telefone, email, endereco, salario)
    
   
        