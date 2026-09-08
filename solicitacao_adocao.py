from estados import EstadoPendente

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from animal import Animal
    from adotante import Adotante
    from estado_solicitacao import EstadoSolicitacao

class SolicitacaoAdocao:

    def __init__(self, animal: Animal, adotante: Adotante):
        self.__animal: Animal = animal
        self.__adotante: Adotante = adotante
        self.__estado: EstadoSolicitacao = EstadoPendente()

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, novo_estado: EstadoSolicitacao):
        self.__estado = novo_estado

    def aprovar(self):
        self.__estado.aprovar(self)
        self.__animal.status = "Adotado"

    def rejeitar(self):
        self.__estado.rejeitar(self)

    def exibir(self):
        return (
            f"{self.__animal.nome} -> "
            f"{self.__adotante.nome} | "
            f"{type(self.__estado).__name__}"
        )
