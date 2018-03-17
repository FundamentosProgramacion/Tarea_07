def calcularDivision(divisor, dividendo):
    cociente= 0
    sobrante=0
    while divisor >= dividendo:
        divisor = divisor - dividendo
        cociente+= 1

    return cociente

def calcularMayor(numero):
    lista=[]
    while numero>=0:
        lista.append(numero)
        numero = int(input("Teclea el número(-1 para salir):"))
    if len(lista)>0:
        print("Mayor:", max(lista))
        list.sort(lista)

    else:
        print("No hay datos")

    return lista



def main():

    print ( "Bienvenido a este menu" )

    print ( """
        1. Imprimir divisiones
        2. Número mayor
        3. Salir
          """ )

    print ( "" )
    seleccion = int ( input ( "¿Qué desea hacer?:" ) )

    while seleccion >= 0:
        if seleccion == 1:
            divisor = int ( input ( "Escribe el divisor:" ) )
            dividendo = int ( input ( "Escribe el dividendo:" ) )

            print("La division de",divisor,"/",dividendo,"es:",calcularDivision(divisor, dividendo))
            seleccion = int ( input ( "¿Qué desea hacer?:" ) )



        elif seleccion == 2:
            print ( "Bienvenido al programa que calcula el número mayor" )
            print ( "Bienvenido al programa que calcula el número mayor" )
            numero = int ( input ( "Teclea el número(-1 para salir):" ) )
            print ( calcularMayor ( numero ))
            seleccion = int ( input ( "¿Qué desea hacer?:" ) )

        elif seleccion == 3:
            print ( "Adios, gracias por usar este programa" )

            break


main()