# Creación de dos coches y dos personas
from coche import Coche
from coche_combustion import CocheCombustion
from coche_electrico import CocheElectrico
from persona import Persona

if __name__ == '__main__':
    # Crear coches
    coche1 = Coche('5996 JML', 'BMW')
    coche2 = Coche('173 MTM', 'Audi')

    # Crear personas
    persona1 = Persona('74018393A', 'Alba', 'Barea', coche1)
    persona2 = Persona('27819021J', 'Liliana', 'Lorca')

    print(persona1)
    print(persona2)
    print(coche1)
    print(coche2)
    persona1.vender_coche(persona2)
    print(persona1)
    print(persona2)
    coche1.avanzar(20)
    coche1.repostar(1)
    coche1.avanzar(20)

    print(coche1.km_recorridos_coche_por_marca('BMW'))

    coche3 = CocheElectrico('1189 LOP', 'MERCEDES')
    coche3.recargar(20,10)
    coche3.recargar(30, 10)


    coche4 = CocheCombustion('4789 APO', 'PORSCHE')
    coche4.avanzar(20)
    coche4.repostar_combustion(30)
    coche4.avanzar_combustion(601)









