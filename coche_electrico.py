# coche_electrico.py
from coche import Coche
class CocheCombustion(Coche):
    def __init__(self, matricula, marca, carga):
        super().__init__(matricula, marca)
        self.carga = carga
