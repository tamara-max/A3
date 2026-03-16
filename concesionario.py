#concesionario.py

class Concesionario:
    def __init__(self, nombre, lista_coches, lista_personas):
        self.nombre = nombre
        self.lista_coches = lista_coches
        self.lista_personas = lista_personas

    def __str__(self):
        return f'nombre: {self.nombre}, coches: {self.lista_coches}'

    def __repr__(self):
        return f'Concesionario(nombre={self.nombre}, coches={self.lista_coches})'

