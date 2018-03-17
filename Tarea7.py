# Autor: Carlos Martíenz Rodírguez
# En este programa se utilizaran ciclos while para resolver problemas

# Función para calcular la división entre dos números mediante el método de resta
def dividir(n, d):
    numerador = n
    denominador = d
    counter = 0
    while numerador >= denominador:
        numerador = numerador - denominador
        counter += 1
    return str(n) + " / " + str(d) + " = " + str(counter) + ", sobra " + str(numerador)

# Encontrar el número mayor de un conjunto proporcionado por el usuario
def encontrarMayor():
    b = 0
    a = 0
    counter = 0
    while a != -1:
        a = int(input("Teclea un número [-1 para salir]: "))
        if a > b:
            b = a
        counter += 1

    if counter == 1:
        result = "No hay valor"
    else:
        result = "El mayor es: " + str(b)
    return result


# Función Main
def main():
    q = 0
    # Menú para seleccionar función del programa
    # Mientras el usuario teclé un número diferente del tres el programa seguirá funcionando
    while (q != 3):
        print("\nTarea 07. Ciclos while \nAutor: Carlos Martínez Rodríguez \n")
        print("1. Imprimir divisiones \n2. Encontrar el mayor \n3. Salir")
        q = int(input("Teclea tu opción: "))
        if (q == 1):
            print("\nBienvenido al programa de divisiones")
            n = int(input("Divisor: "))
            d = int(input("Dividendo: "))
            print(str(dividir(n,d)))
        elif (q == 2):
            print("\nBienvenido al programa que encuentra el mayor")
            print(encontrarMayor())
        elif (q == 3):
            print("\nGracias por usar este programa, regresa pronto.")
        else:
            print("\nERROR, teclea 1, 2 o 3")

main()