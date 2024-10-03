import sys
sys.path.append("/workspaces/Atividade-em-equipe")

from project.models.enums.UnidadeFederativa import UnidadeFederativa

class Endereco():
    def __init__(self, logradouro:str, numero:str, complemento:str, uf:UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.uf = uf

    def __str__(self) -> str:
        return ( 
                f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nUnidade Federativa: {self.uf.nome}"
                )

endereco = Endereco("Rua BEILA", "130", "1º Andar", UnidadeFederativa.BAHIA)
print(endereco)