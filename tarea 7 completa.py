##Autor: David Medina Medina A01653311
##Divisiones sin operandos /,//,%, encontrar mayor y menu.

def probarDivisiones(dividendo,divisor):
    a = 0
    while dividendo>=divisor:
        dividendo = dividendo-divisor
        a += 1
    print('\n')
    print(n1,"/", n2, "=", a, ", sobra", dividendo,'\n')

def encontrarMayor(lista):
    nMayor = max(lista)
    return nMayor

def main():
    lista = []
    print("Tarea 07. Ciclos while")
    print("Autor: David Medina Medina.")
    print('\n'"Seleccione 1 para imprimir divisiones.")
    print("Seleccione 2 para encontrar mayores.")
    print("Seleccione 3 para salir.")
    opcion = int(input("Seleccione que quiere hacer: "))
    while opcion >= 1 and opcion <=3:
        if opcion ==1:
            global n1
            n1 = int(input("Ingresar dividendo: "))
            global n2
            n2 = int(input("Ingresar divisor: "))
            probarDivisiones(n1, n2)
            main()
            

        if opcion ==2:
            numero = int(input("Seleccione numero: para saber el numero mayor ingresar [-1]: "))
            if numero ==-1:
                print ("No hay valor mayor!"'\n')
                main()
  
            while numero != -1:
                lista.append(numero)
                numero = int(input("Seleccione numero, para saber el numero mayor ingresar [-1]: "))
            print("El numero mayor es:", encontrarMayor(lista), '\n')
            main()
            

        if opcion ==3:
            print("Gracias por usar este programa, regrese pronto.")
            break

    else:
        print ("¡¡¡Error, teclea del 1 al 3!!!")
        print('\n')
        main()
main()

