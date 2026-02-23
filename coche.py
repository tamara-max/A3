# coche.py
class Coche:
    km_por_marca = {}
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0
        self.gasolina = 0


        if marca not in Coche.km_por_marca:
            type(self).km_por_marca[marca] = 0


    def __str__(self):
        return (f'Coche: {self.matricula} ({self.marca}) - km : {self.kilometros_recorridos} km')

    def __repr__(self):
            return (f'coche(matricula-{self.matricula!r}, marca-{self.marca!r},')

    def avanzar(self, km):
        total = 0.05 * km
        if self.gasolina >= total:
            self.kilometros_recorridos += km
            type(self).km_por_marca[self.marca] += km
            self.gasolina -= total
            print(f'Has avanzado: {km} km')

        else:
            print('No queda suficiente gasolina')

    def repostar(self, litros):
        self.gasolina += litros
        print(f'Gasolina repostada: {litros} L')


    @classmethod
    def km_recorridos_coche_por_marca(cls, marca):
        recorridos = cls.km_por_marca[marca]
        return f'La marca: {marca} ha recorrido {recorridos} km '






