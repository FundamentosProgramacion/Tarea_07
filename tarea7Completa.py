# Autor: Diana Aguilar Mtz
# Descripcion:

#funcion 1: hace divisiones y te muestra el residuo.
def probarDivisores():
    print("                               ")
    print("Bienvenido al programa de divisores")
    divisor = int(input("Divisor: "))
    dividendo = int(input("Dividendo: "))
    resultado = dividendo // divisor #cociente
    modulo = dividendo % divisor #residuo
    print(dividendo, "/", divisor, "=", resultado, ", sobra: ", modulo)

# funcion 2: te muestra el numero mayor que hayas ingresado, sin saber cuando vas a parar.
def determinarMayor():
    print("                               ")
    print("Bienvenido al programa que encuentra el mayor")
    n = int(input("Teclee un número [-1 para salir]: "))
    numeroMayor = 0 #valor inicial
    if n ==-1: #opcion para salir cuando no han metido ningun numero.
        print("No hay numero mayor")

    elif n != -1: #opcion para comparar numeros.
        while n != -1:
            n = int(input("Teclee un número [-1 para salir]: "))
            if n > numeroMayor:
                numeroMayor = n
        print("el numero mayor es: ", numeroMayor)



def main():
    print("""Tarea 7: Ciclos While 
Autor: Diana Aguilar Mtz. 

1: Imprimir divisores 
2: Encontrar el mayor 
3: Salir """)

    opcion = int(input("Teclea tu opción: ")) #el ususario decide que desea hacer.

    while opcion >0: #while principal mostrar menú.
        if opcion == 1:
            probarDivisores()# funcion 1.

        elif opcion == 2:
            determinarMayor()#funcion 2.

        elif opcion == 3: #funcion para sair del programa.
            break

        else:
            print("ERROR, teclea 1, 2 o 3") #mensaje que aparece cuando seleccionas un numero mayor a 3.


        print("""
Tarea 7: Ciclos While 
Autor: Diana Aguilar Mtz. 

1: Imprimir divisores 
2: Encontrar el mayor 
3: Salir """)
        opcion = int(input("Teclea tu opción: "))


    print("                               ")
    print("Gracias por usar este programa, vuelve pronto") #mensaje de despedida


main()

