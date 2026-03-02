# coche_electrico.py
from coche import Coche

class CocheElectrico(Coche):
    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)
        self.carga = 0


    # def consumir(self):
    #     total = 0.02*self.avanzar()
    #     self.carga -= total
    #     print(f'Has recorrido: {self.avanzar()}, y tu carga se ha reducido: {total}')
    #     print(f'Carga actualizada: {self.carga}')



    def recargar(self, cantidad,km = 0):
        total = 0.02 * km
        if self.carga > 0:
            self.carga -= total
            print(f'Has recorrido: {km} km  y tu carga se ha reducido: {total}%')
        else:
            print('No tienes carga para avanzar. ¡RECARGA!')
        print(f'Tienes {self.carga}%')
        self.carga += cantidad
        print(f'Has recargado: {cantidad}%, carga actualizada: {self.carga}%')




