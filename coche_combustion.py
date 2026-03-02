# coche_combustion.py
from coche import Coche
class CocheCombustion(Coche):
    def __init__(self, matricula, marca, combustion):
        super().__init__(matricula, marca)
        self.combustion = combustion



