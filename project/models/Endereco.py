
from project.enums import UnidadeFederativa


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
                f"\nUnidade Federativa: {self.uf}"
                )

