# persona.py
class Persona:
    def __init__(self, dni, nombre, apellido, coche = None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.coche = coche


        def __str__(self):
            cad = f'Persona {self.nombre} ({self.apellido} -dni: {self.dni})'

            return cad