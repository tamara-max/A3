# coche_combustion.py
from coche import Coche
class CocheCombustion(Coche):
    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)


    def repostar(self):
        super().avanzar()
        super().repostar()



