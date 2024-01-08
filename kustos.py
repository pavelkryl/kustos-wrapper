from abstract_kustos import AbstractKustos, Karta

class Kustos(AbstractKustos):

    def __init__(self) -> None:
        self._nazdar = "nazdar"

    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Karta | None:
        return None

    def odeber_kartu(self, id_karty: str) -> Karta | None:
        return None

    def muze_vstoupit(self, id_karty: str) -> bool:
        return False