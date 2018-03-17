
def dividirEsquinas(numero):
    for x in range(1, 361, 360//numero):
        print(x-1)


def main():
    variable = int(input('Teclea la cantidad de esquinas: '))
    dividirEsquinas(variable)

main()