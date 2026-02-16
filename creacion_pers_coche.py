# Creación de dos coches y dos personas
import Coche from coche.py
import Persona from persona.py

if __name__ == '__main__':
    # Crear coches
    coche1 = coche.Coche('5996 JML', 'BMW', 200000, 50)
    coche2 = coche.Coche('173 MTM', 'Audi', 38000, 71)

    # Crear personas
    persona1 = Persona.Persona('74018393A', 'Alba', 'Barea', coche1)
    persona2 = Persona.Persona('27819021J', 'Liliana', 'Lorca')

    print(persona1)
    print(persona2)
    print(coche1)
    print(coche2)





