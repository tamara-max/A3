# coche_electrico.py
from coche import Coche

class CocheElectrico(Coche):
    def __init__(self, matricula, marca, carga):
        super().__init__(matricula, marca)
        self.carga = carga


    def consumir(self, total):
        total = 0.02*self.avanzar()
        self.carga -= total
        print(f'Has recorrido: {self.avanzar()}, y tu carga se ha reducido: {total}')
        print(f'Carga actualizada: {self.carga}')



    def recargar(self, cantidad):
        print(f'Tienes {self.carga}%')
        self.carga += cantidad
        print(f'Has recargado: {cantidad}%, carga actualizada: {self.carga}%')




