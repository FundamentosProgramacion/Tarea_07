# encoding: UTF-8
# Autor: Alejandro Valenzuela Guerrero

def divisiones(a,b):
    a = a
    c = 0
    while a >= b:
        a = a - b
        c = c + 1
        if b > a or a == 0:
            print("El cociente es:", c)
            print("El residuo es:", a)

def numMayor():
    x = 0
    y = int(input("Teclea un número:"))
    if y != -1:
        while y != -1:
            x = x + (y - x)
            y = int(input("Teclea un número"))
            if y == -1:
                print("El número mayor es:", x)
    else:
        print("No hay valor mayor")

def main():
    print("1.Imprimir divisiónes")
    print("2.Encontrar el mayor")
    print("3.Salir")
    x = int(input("Teclea tu opción:"))
    if x == 1:
        dividendo = int(input("Escribe el numero a dividir:"))
        divisor = int(input("Escribe el número entre el cual dividir:"))
        divisiones(dividendo,divisor)
    if x == 2:
        numMayor()
    if x == 3:
        print("Gracias por usar este programa, regresa pronto.")
    if x < 1 or x > 3:
        print("Error, teclea 1, 2 o 3")

main()