# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_07: Ciclos WHILE
from getpass import getuser as get
user = get()

def imprimirDivisores():




def main():
    eleccion = int(input('Tarea_07: Ciclos WHILE\n'
                        'Autor: Sebastian Morales Martin\n'
                        'Bienvenido %s !!!\n'
                         '' % user))
    while eleccion <= 3 and eleccion > 0:
        if eleccion == 1:
            imprimirDivisores()
        elif eleccion == 2:
            encontrarMayor()
        elif eleccion == 3:
            print('Gracias por usar este programa, regresa pronto %s.'% user)


main()
