# Autor José Francisco Murillo Lozano A01374561
# Resulve la tarea 7 de Fundamentos de programación


def dividir(divisor, dividendo):
    cociente = 0
    while divisor <= dividendo:
        cociente += 1
        dividendo -= divisor
    division = [cociente, dividendo]
    return division



def main():
    print("Tarea 7 Ciclos while")
    print("Autor: José Francisco Murillo Lozano")
    print("1. Imprimir divisiones")
    print("2. Encontrar el valor mayor")
    print("3. Salir")
    menu = input("Teclea tu opción: ")
    if menu.strip():
        menu1 = int(menu)
        if menu1 != 3:
            while menu1 != 3:
                menu1 = int(menu1)
                if menu1 != 2 and menu1 != 1:
                    print("ERROR, teclea 1, 2 o 3")

                if menu1 == 1:
                    print("\nBienvenido al programa de Divisiones")
                    divisor = int(input("Divisor: "))
                    dividendo = int(input("Dividendo: "))
                    division = dividir(divisor, dividendo)
                    print(dividendo, "/", divisor, "=", division[0], ", sobra", division[1])

                if menu1 == 2:
                    print("\nBienvenido al programa que encuentra el valor mayor")
                    valor = int(input("Teclea un número [-1 para salir]: "))
                    if valor == -1:
                        print("No hay valor mayor")
                    valores = []
                    while valor != -1:
                        valores.append(valor)
                        valor = int(input("Teclea un número [-1 para salir]: "))
                    if len(valores) != 0:
                        print("El mayor es:", max(valores))

                print("\nTarea 7 Ciclos while")
                print("Autor: José Francisco Murillo Lozano")
                print("1. Imprimir divisiones")
                print("2. Encontrar el valor mayor")
                print("3. Salir")
                menu1 = int(input("Teclea tu opción: "))

    print("\nGracias por usar este programa, regresa pronto.")


main()
