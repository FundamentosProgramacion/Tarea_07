# Author: Guillermo Adrian Urbina Aguiñiga
# Tarea07

def encontrarMayor():
    listanumero = []
    numero = int(input("Teclea un número [-1 para salir]: "))
    while numero != -1 :
        listanumero.append(numero)
        numero = int(input("Teclea un número [-1 para salir]: "))

    print("El mayor es: ", max(listanumero))

def probarDivisiones():
    print("Bienvenido al programa de divisor")
    divisor = int(input("Divisor: "))
    dividendo = int(input("Dividendo: "))
    divisor2 = divisor
    veces = 0
    residuo = divisor
    while divisor >= dividendo and divisor >= 0:
        divisor = divisor - dividendo
        veces = veces + 1
        residuo = divisor
    print(divisor2, " / ", dividendo, " = ", veces, ", ", "sobra " ,residuo)

def main():
    print("1. Imprimir divisiones")
    print("2. Encontrar el mayor")
    print("3. salir")
    a = int(input("Teclea tu opción: "))
    if a == 1:
        probarDivisiones()
    elif a == 2:
        encontrarMayor()
    elif a == 3:
        print("Gracias por usar este programa, regresa pronto")

main()
