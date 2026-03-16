import concesionario
from coche import Coche
from coche_combustion import CocheCombustion
from coche_electrico import CocheElectrico
from coche_hibrido import CocheHibrido
from persona import Persona
from concesionario import Concesionario


if __name__ == '__main__':

    print('\n--- CREACIÓN DE COCHES Y PERSONAS ---')

    # Crear coches (ahora deben ser de clases concretas)
    coche1 = CocheCombustion('5996JML', 'BMW')
    coche2 = CocheCombustion('173MTM', 'Audi')

    # Crear personas
    persona1 = Persona('74018393A', 'Alba', 'Barea', coche1)
    persona2 = Persona('27819021J', 'Liliana', 'Lorca')

    print(persona1)
    print(persona2)


    print('\n--- PRUEBA DE VENTA DE COCHE ---')

    persona1.vender_coche(persona2)

    print(persona1)
    print(persona2)


    print('\n--- PRUEBA AVANZAR SIN GASOLINA ---')

    coche1.avanzar(20)


    print('\n--- REPOSTAR Y AVANZAR ---')

    coche1.repostar(5)
    coche1.avanzar(20)

    print(coche1)


    print('\n--- KM TOTALES POR MARCA ---')

    print(Coche.km_recorridos_coche_por_marca('BMW'))
    print(Coche.km_recorridos_coche_por_marca('Audi'))


    print('\n--- PRUEBA COCHE ELÉCTRICO ---')

    coche3 = CocheElectrico('1189LOP', 'Mercedes')

    coche3.avanzar(10)   # sin batería
    coche3.recargar(10)  # recargar
    coche3.avanzar(10)   # ahora sí


    print('\n--- PRUEBA COCHE COMBUSTIÓN ---')

    coche4 = CocheCombustion('4789APO', 'Porsche')

    coche4.avanzar(10)   # sin gasolina
    coche4.repostar(10)  # repostar
    coche4.avanzar(50)   # avanzar


    print('\n--- KM POR MARCA ACTUALIZADOS ---')

    print(Coche.km_recorridos_coche_por_marca('BMW'))
    print(Coche.km_recorridos_coche_por_marca('Mercedes'))
    print(Coche.km_recorridos_coche_por_marca('Porsche'))


    print('\n--- PRUEBA COCHE HÍBRIDO ---')

    coche5 = CocheHibrido('4587ABC', 'Toyota')


    print('\nRECORRIDO SIN ENERGÍA')
    coche5.avanzar(10)


    print('\nCARGAMOS BATERÍA')
    coche5.recargar(10)

    coche5.avanzar(50)


    print('\nSIN BATERÍA → USAR GASOLINA')

    coche5.repostar(10)

    coche5.avanzar(50)

    print('\n--- PRUEBA CONCESIONARIO ---')
    concesionario1 = Concesionario('Cochfast',[coche4, coche5])

    print('\nCantidad de coches en el concesionario1')
    print(len(concesionario1))

    print('\nPrimer coche del concesionario')
    print(concesionario1[0])

    print('\nSegundo coche del concesionario')
    print(concesionario1[1])

    print('\n¿Hay coches?')

    if concesionario1:
        print('El concesionario tiene coches')
    else:
        print('El concesionario está vacío')

    concesionario2 = Concesionario('Cochius')
    print('\n¿Hay coches en concesionario2?')

    if concesionario2.len(concesionario1) > 0:
        print('El concesionario tiene coches')
    else:
        print('El concesionario está vacío')

