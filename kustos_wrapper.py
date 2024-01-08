from typing import Optional
from abstract_kustos import AbstractKustos, Karta


class KustosWrapper(AbstractKustos):

    def __init__(self, delegate: AbstractKustos):
        self._delegate = delegate

    def muze_vstoupit(self, id_karty: str) -> bool:
        pass

    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Karta | None:
        pass

    def odeber_kartu(self, id_karty: str) -> Karta | None:
        pass