# coche_electrico.py
from coche import Coche

class CocheElectrico(Coche):

    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)
        self.carga = 0

    def recargar(self, cantidad):
        self.carga += cantidad
        print(f'Carga actual: {self.carga} kWh')

    def avanzar(self, km):
        consumo = 0.02 * km

        if self.carga >= consumo:
            self.kilometros_recorridos += km
            type(self).km_por_marca[self.marca] += km
            self.carga -= consumo
            print(f'El coche eléctrico avanzó {km} km')
        else:
            print('No hay suficiente carga')
