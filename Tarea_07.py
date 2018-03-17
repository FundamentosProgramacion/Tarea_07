#Mirna Fernanda Zertuche Calvillo
#Tarea 07
#Un programa que a traves de un menu realiza una división o identifica el número mayor de un listado

def calcularDivisión(divisor, dividendo):
    cosciente = 0
    # Resta
    while divisor >= dividendo:
        divisor = divisor - dividendo
        cosciente = cosciente + 1

    return cosciente
def calcularMayor():
    valor = -1
    valor2 = 0
    while valor2 != -1:
        valor2 = int(input("Teclea un número [-1 para salir]: "))
        if valor < valor2:
            valor = valor2
        else:
            valor = valor

    return (valor)



def main():
    accion = 1
    while  accion != 3:
        accion = int(input("1. Imprimir divisiones\n2. Encontrar mayor\n3. Salir\nTeclea tu opción: "))
        if accion == 1:
            divisor = int(input("Divisor: "))
            dividendo = int(input("Dividendo: "))
            cosciente = calcularDivisión(divisor, dividendo)
            sobra = divisor - (cosciente * dividendo)
            print(divisor, "/", dividendo, "=", cosciente, ",sobra", sobra)
        elif accion== 2:#Calcula mayor
            mayor= calcularMayor()
            if mayor==-1:
                print("No hay valor mayor")
            else:
                print( "El mayor es:",mayor)





main()

