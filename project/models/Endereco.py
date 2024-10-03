import sys
sys.path.append("workspaces/Atividade-Em-Equipe/project")
from project.models.enums.UnidadeFederativa import UnidadeFederativa

class Endereco():
    def __init__(self, logradouro:str, numero:str, complemento:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento

    