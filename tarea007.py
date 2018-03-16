
def dividir(dividendo,divisor):
    count = 0

    while dividendo >= divisor:
        resta = dividendo-divisor
        dividendo = resta
        count = count + 1
    print ("sobra "+str(dividendo))

    return ("resultado = " +str(count))

def mayor():
    lista = []
    dato= int(input("Teclea un valor [-1 termina]: "))
    while dato != -1:
        lista.append(dato)
        dato = int(input("Teclea un valor [-1 termina]: "))
    if lista == []:
        print ("No hay valor mayor: ")
    else:
        print("El mayor es: " +str(max(lista)))

def main():
    answer= int(input("1.Imprimir divisores: " "\n2.Encontar el mayor: " "\n3.Salir" "\n"))
    if answer == 1:
        a = int(input("Teclea dividendo: "))
        b = int(input("Teclea divisor: "))
        resultado = dividir(a, b)
        print resultado

    if answer == 2:
        mayor()

    if answer == 3:
        print ("Gracias por usar mi programa, regresa las veces que quieras. ")

    else:
        print("ERROR ERROR ERROR, por favor teclea 1, 2 o 3")

main()