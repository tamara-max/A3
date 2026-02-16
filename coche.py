# coche.py
class Coche:
    km_por_marca = {}
    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0
        self.gasolina = 0

        if marca not in Coche.km_por_marca:
            Coche.km_por_marca[marca] = 0


    def __str__(self):
        return (f'Coche: {self.matricula} ({self.marca}) - km : {self.kilometros_recorridos} km')

    def __repr__(self):
            return (f'coche(matricula-{self.matricula!r}, marca-{self.marca!r},'
                    f'kilometros-{self.kilometros_recorridos!r}, gasolina-{self.gasolina!r}')




    coches = {}
    coches['Marca'] = marca
    coches['Kilometros'] = kilometros_recorridos

    for marca in coches:
        if marca == coches['Marca']:
            coches['kilometros'] += kilometros_recorridos



