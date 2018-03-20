#Autor: Nataly Paulina Lopez Salazar
#Descripcion: Tarea 7 con while.


def probarDivisiones(divisor, dividendo):
    ct = 0
    cociente = divisor -dividendo
    while(dividendo>=divisor):
        ct += 1
        dividendo = dividendo - divisor
    return ct


def calcularMayor(num):
    ct = 0
    while num>num:
        print(num)
    ct+=1
    return num


def main():
    print("Menu")
    print("1. Imprimir divisiones")
    print("2. Econtrar el mayor ")
    print("3. Salir")
    n = int(input("Teclea tu opción: "))

    if n==1:
        print("Bienvenido al programa de divisiones")
        dividendo= int(input("Valor de tu dividendo:"))
        divisor= int(input("Valor de tu divisor:"))
        cociente= probarDivisiones(divisor,dividendo)
        print(dividendo,"/",divisor,"=",cociente)

    if n==2:
        print("Bienvenido al programa que encuentra el mayor")
        num = int(input("Teclea el numero[-1 para terminar]:"))
        mayor = calcularMayor(num)
        print("El mayor es:",mayor)

        if num == -1:
                print("No hay numero mayor")



    while n !=3 :
        print("Menu")
        print("1. Imprimir divisiones")
        print("2. Econtrar el mayor ")
        print("3. Salir")
        n = int(input("Teclea tu opción:"))



main()