class Adotante:
    def __init__(self, nome: str, cpf: str, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    def exibir_dados(self):
        return (
            f"Nome: {self.__nome} | "
            f"CPF: {self.__cpf} | "
            f"Telefone: {self.__telefone}"
        )
