# coche_combustion.py
from coche import Coche
class CocheCombustion(Coche):
    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)
        self.combustion = 0


    def repostar_combustion(self, litros = 0):
        super().repostar(litros)

    def avanzar_combustion(self, km):
        super().avanzar(km)
        self.combustion -= km


