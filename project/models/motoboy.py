

from project.abstracts.Pessoa import Pessoa


class motoboy(Pessoa):
    def __init__(self, nome, telefone, email, endereco):
        super().__init__(nome, telefone, email, endereco)