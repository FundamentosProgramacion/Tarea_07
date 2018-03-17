# Autor: Andrés Reyes Rangel.
# Descripción: Calcula la división de un número solamente restando y el mayor número de una lista.

def encontrarMayor(numero):
    lista = []  # crea una lista sin datos
    while numero != -1:  # No pide terminar
        lista.append(numero)
        numero = int(input("Ingresa un valor [-1 termina]: "))
    if len(lista) > 0:
        return "El mayor es: %d" % max(lista)
    else:
        return "No hay valor"

def main():
    print("Tarea 07. Ciclos While\n"
          "Autor: Andrés Reyes Rangel\n"
          "\n"
          "1. Imprimir divisiones\n"
          "2. Encontrar el mayor\n"
          "3. Salir\n")
    opcion = int(input("Teclea tu opción: "))
    print("____________________________________________\n")

    while opcion != 3:
        if opcion != 1 and opcion != 2:
            print("ERROR, elije 1, 2 o 3")
        elif opcion == 1: #Imprime una división
            print("Bienvenido al programa de divisiones")
            divisor = int(input("Ingrese el divisor: "))
            dividendo = int(input("Ingrese el dividendo: "))
            residuo = divisor - dividendo
            cociente = 1
            while residuo >= dividendo:
                residuo -= dividendo
                cociente += 1
            print("%d / %d = %d, sobra %d" % (divisor, dividendo, cociente, residuo))
        elif opcion == 2: #Encuentra el número mayor
            print("Bienvenido al programa que encuentra el número mayor")
            numero = int(input("Ingresa un número [-1 termina]: "))
            mayor = encontrarMayor(numero)
            print(mayor)

        #Imprime el menú las veces que se repita el programa
        print("____________________________________________\n")
        print("Tarea 07. Ciclos While\n"
              "Autor: Andrés Reyes Rangel\n"
              "\n"
              "1. Imprimir divisiones\n"
              "2. Encontrar el mayor\n"
              "3. Salir\n")
        opcion = int(input("Teclea tu opción: "))
        print("____________________________________________\n")
    print("Gracias por usar este programa, vuelve pronto")
main()
