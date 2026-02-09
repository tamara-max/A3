def leer_notas():
    entrada = input('Introduce las notas separadas por espacios: ')
    notas_str = entrada.split()
    notas = [float(nota) for nota in notas_str]
    return notas


def calcular_media(notas):
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)


def mostrar_resumen(notas):
    if len(notas) == 0:
        print('No se han introducido notas.')
        return

    print(f'Número de notas: {len(notas)}')
    print(f'Nota máxima: {max(notas)}')
    print(f'Nota mínima: {min(notas)}')
    print(f'Nota media: {calcular_media(notas)}')


if __name__ == '__main__':
    notas = leer_notas()
    mostrar_resumen(notas)





