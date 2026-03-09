# coche.py
from abc import ABC, abstractmethod

class Coche(ABC):
    __km_por_marca = {}
    def __init__(self, matricula, marca):
        self.__matricula = matricula
        self.__marca = marca
        self.__kilometros_recorridos = 0

        if marca not in Coche.__km_por_marca:
            type(self).__km_por_marca[marca] = 0

    # Propiedades
    @property
    def matricula(self):
        return self.__matricula

    @property
    def marca(self):
        return self.__marca

    @property
    def kilometros_recorridos(self):
        return self.__kilometros_recorridos

    # Metodo protegido para sumar km
    def _sumar_km(self, km):
        self.__kilometros_recorridos += km
        type(self).__km_por_marca[self.__marca] += km

    def __str__(self):
        return (f'Coche: {self.matricula} ({self.marca}) - km : {self.kilometros_recorridos} km')

    def __repr__(self):
            return f'Coche(matricula={self.matricula!r}, marca={self.marca!r})'

    @abstractmethod
    def avanzar(self, km):
        pass
        # total = 0.05 * km
        # if self.gasolina >= total:
        #     self.kilometros_recorridos += km
        #     type(self).km_por_marca[self.marca] += km
        #     self.gasolina -= total
        #     print(f'Has avanzado: {km} km')
        #     return km
        #
        # else:
        #     print('No queda suficiente gasolina')

    # def repostar(self, litros):
    #     self.gasolina += litros
    #     print(f'Gasolina repostada: {litros} L')


    @classmethod
    def km_recorridos_coche_por_marca(cls, marca):
        recorridos = cls.__km_por_marca[marca]
        return f'La marca: {marca} ha recorrido {recorridos} km '






