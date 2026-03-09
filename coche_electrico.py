# coche_electrico.py
from coche import Coche

class CocheElectrico(Coche):

    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)
        self.__carga = 0

    def recargar(self, cantidad):
        self.__carga += cantidad
        print(f'Carga actual: {self.__carga} kWh')

    @property
    def carga(self):
        return self.__carga

    def avanzar(self, km):
        consumo = 0.02 * km

        if self.carga >= consumo:
            self._sumar_km(km)
            self.__carga -= consumo
            print(f'El coche eléctrico avanzó {km} km')
        else:
            print('No hay suficiente carga')
