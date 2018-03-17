# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_07: Ciclos WHILE
from getpass import getuser as get
user = get()

def imprimirDivisores(dividendo, divisor):  #funcion que usa el metodo de restar el divisor al dividendo cuantas veces se pueda para determinar el cociente y el residuo
    residuo = dividendo
    cociente = 0
    if divisor == 0:        # agregue esto para evitar errores matematicos en el codigo
        return '\nMATH ERROR\n\n'
    while (residuo - divisor) >= 0:
        residuo -= divisor
        cociente += 1
    return'\n%s / %s = %s, sobra %s\n\n'% (dividendo, divisor, cociente, residuo)



def encontrarMayor():           # encuentra el numero mayor de una serie de numeros dados (si el numero dado es mayor al almacenado, el almacenado se iguala a 0 para borrarse y se le suma el nuevo numero hasta que se decida cerrar la funcion)
    mayor = 0
    numero = int(input('Teclea un número (teclea "-1" para salir): '))
    if numero == -1:
        return 'No hay numero mayor.'
    while numero != -1:
        if numero > mayor:
            mayor = 0
            mayor += numero
        numero = int(input('Teclea un número (teclea "-1" para salir): '))
    return 'El mayor es: %s\n\n' % mayor


def main():
    eleccion = int(input('Tarea_07: Ciclos WHILE\n'
                         'Autor: Sebastian Morales Martin\n'
                         'Bienvenido %s !!!\n\n'
                         '1. Imprimir divisiones\n'
                         '2. Encontrar el mayor\n'
                         '3. Salir\n'
                         'Teclea tu opcion: ' % user))

    while eleccion != 3:
        if eleccion == 1:
            print('\nPrograma de divisiones')
            dividendo = int(input('\nDividendo: '))
            divisor = int(input('Divisor: '))
            print(imprimirDivisores(dividendo, divisor))
        elif eleccion == 2:
            print(encontrarMayor())
        else:
            print('\nERROR. Teclea 1, 2 o 3.\n')
        eleccion = int(input('Tarea_07: Ciclos WHILE\n'
                             'Autor: Sebastian Morales Martin\n'
                             'Bienvenido %s !!!\n\n'
                             '1. Imprimir divisiones\n'
                             '2. Encontrar el mayor\n'
                             '3. Salir\n'
                             'Teclea tu opcion: ' % user))
    print('Gracias por usar este programa, regresa pronto %s.' % user)
        


main()
