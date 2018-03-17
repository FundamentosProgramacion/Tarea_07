#Jossian Abimelec García Quijano
#Determina la división por la resta del divisor y determina el mayor de los numeros ingresados por el usario

def dividir(dividendo,divisor):
    
    contador=0
    operacion=dividendo
    while operacion>=divisor:
        operacion=operacion-divisor
        contador+=1
    print(dividendo,"/",divisor,"=",contador,", sobra",operacion)

def mayor(numero, lista):
    while numero !=-1:
        lista.append(numero)
        numero = int(input("""Bienvenido al programa que encuentra el mayor 
            Teclea un número [-1 para salir]: """))
        print("El mayor es: ", max(lista))

def main():
    opcion=int(input("""1.Imprimir divisiones
2.Encontrar el mayor
3.Salir
Teclea tu opción: """))

    if opcion==1:
        print("bienvenido al programa de divisiones")
        divisor=int(input("Divisor: "))
        dividendo = int(input("Dividendo: "))
        dividir(divisor,dividendo)

    elif opcion==2:
        lista = []
        numero = int(input("""Bienvenido al programa que encuentra el mayor 
Teclea un número [-1 para salir]: """))

        if numero == -1:
            print("No hay valor mayor")

        mayor(numero,lista)

    elif opcion==3:

        print("Gracias por usar este programa, regresa pronto.")
    else:
        print("Error, teclea 1 2 o 3")


    
main()