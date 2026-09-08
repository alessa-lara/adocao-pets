from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from animal import Animal
    from solicitacao_adocao import SolicitacaoAdocao

class Abrigo:

    __instancia = None

    def __new__(cls, nome: str):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def __init__(self, nome: str):
        if not hasattr(self, "_inicializado"):
            self.__nome: str = nome
            self.__animais: list[Animal] = []
            self.__solicitacoes: list[SolicitacaoAdocao] = []
            self._inicializado: bool = True

    def cadastrar_animal(self, animal: Animal):
        self.__animais.append(animal)

    def cadastrar_solicitacao(self, solicitacao: SolicitacaoAdocao):
        self.__solicitacoes.append(solicitacao)

    def listar_animais(self):
        for indice, animal in enumerate(self.__animais):
            print(f"{indice} - {animal.exibir_dados()}")

    def listar_solicitacoes(self):
        for indice, solicitacao in enumerate(self.__solicitacoes):
            print(f"{indice} - {solicitacao.exibir()}")

    @property
    def nome(self):
        return self.__nome

    @property
    def animais(self):
        return self.__animais

    @property
    def solicitacoes(self):
        return self.__solicitacoes
