# persona.py
class Persona:
    def __init__(self, dni, nombre, apellido, coche = None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.coche = coche


    def __str__(self):
        cad = f'Persona {self.nombre} ({self.apellido} -dni: {self.dni})'
        if self.coche:
            cad += f', Su coche: {self.coche.matricula} ({self.coche.marca})'

        return cad

    def vender_coche(self, a_persona):
        #Comprobar que el vendedor tiene coche
        if self.coche == None:
            print('No tienes coche para vender...')
            return False

        #Combrobar que el comprador no tiene coche
        if a_persona.coche != None:
            print(f'{a_persona} ya tienes coche...')
            return False

        a_persona.coche = self.coche
        self.coche = None

        print(f'{self.nombre} ha vendido correctamente su coche a {a_persona.nombre}')
        return True






