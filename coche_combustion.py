# coche_combustion.py
from coche import Coche

class CocheCombustion(Coche):
    def __init__(self, matricula, marca):
        super().__init__(matricula, marca)
        self.__gasolina = 0

    def repostar(self, litros):
        self.__gasolina += litros
        print(f'Gasolina actual: {self.__gasolina} L')

    def avanzar(self, km):
        consumo = 0.05 * km

        if self.__gasolina >= consumo:
            self.__gasolina -= consumo
            self._sumar_km(km)
            print(f'Coche combustión ha avanzado {km} km')
        else:
            print('No queda suficiente gasolina')



