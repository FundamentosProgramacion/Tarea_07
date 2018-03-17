def dividir(divisor, dividendo):
    n=0
    residuo=divisor
    while dividendo>=divisor:
        n=n+1
        dividendo=dividendo-divisor
        sobra=residuo-divisor
    return (n)

def main():
    print("1ºImprimir divisiones")
    print("2ºBuscar el mayor")
    print("3ºSalir")
    opcion=int(input("Que desea hacer? "))
    if opcion !=1 or opcion !=2:
        print("No es una opcion")

    while opcion != 3:
        if opcion==1:
            print("Bienvenido al programa divisor")
            divisor=int(input("Divisor: "))
            dividendo=int(input("Dividendo: "))
            cociente=dividir(divisor, dividendo)
            print(dividendo, "/", divisor, "=", cociente)

        if opcion==2:
            print("Bienvenido al programa mayor")
            lista = []
            dato = int(input("Teclea un valor: [-1 termina]: "))
            while dato != -1:
                lista.append(dato)
                dato = int(input("Teclea un valor: [-1 termina]: "))

            print("Mayor: ", max(lista))

        opcion = int(input("Que desea hacer? "))
    print("Gracias por usar este programa")

main()


