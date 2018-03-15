#Fernando Sebastian Silva M
#Da un menu de finciones que puedes utilizar. Tambien te permite salir manuelmente del programa.


def probarDivisiones(): #Realiza divisiones con restas.
    x = int(input("Dame el Divisor: "))
    y = int(input("Dame el Dividendo: "))
    residuo = x - y
    c = 1

    if y == 0:
        return ("%i / %i = ERROR , sobra ERROR" % (x, y))

    if residuo < 0:
        c = 0
        residuo = x

    elif residuo == 0:
        c = 1

    else:
      while residuo > 0:
        residuo -= y
        if residuo < 0:
            residuo += y
            break
        c += 1

    return("%i / %i = %i, sobra %i" %(x, y, c, residuo))


def encontrarMayor(): #De una lista de datos, busca el numero más alto
    x = int(input("Teclea un numero [teclea -1 para terminar]: "))
    y = x
    if x == -1:
        return("No hay numeros mayores")
    while x != -1:
        if x > y:
            y = x
        x = int(input("Teclea un numero [teclea -1 para terminar]: "))
    else:
        return "El numero mayor es "+str(y)


def main():
    x = int(input(
        "Tarea 07. Ciclos While\nAutor: Fernando S. Silva\n1. Imprimir divisiones\n2.Encontrar el mayor\n3.Salir\nTeclea tu opcion: "))
    while x != 3:
        if x ==1:
            print(probarDivisiones())
            x = int(input(
                "Tarea 07. Ciclos While\nAutor: Fernando S. Silva\n1. Imprimir divisiones\n2.Encontrar el mayor\n3.Salir\nTeclea tu opcion: "))

        elif x == 2:
            print(encontrarMayor())
            x = int(input(
                "Tarea 07. Ciclos While\nAutor: Fernando S. Silva\n1. Imprimir divisiones\n2.Encontrar el mayor\n3.Salir\nTeclea tu opcion: "))

        else:
            print("Error, Teclea 1, 2 ó 3")
            x = int(input(
                "Tarea 07. Ciclos While\nAutor: Fernando S. Silva\n1. Imprimir divisiones\n2.Encontrar el mayor\n3.Salir\nTeclea tu opcion: "))

    print("Gracias por usar el programa, vuelva pronto")

main()


