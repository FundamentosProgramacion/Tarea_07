#Jossian Abimelec García Quijano
#Encuentra el mayor entre los valores que encuentre el usuario

def main():
    lista=[]

    numero=int(input("""Bienvenido al programa que encuentra el mayor 
    Teclea un número [-1 para salir]: """))
    while numero !=-1:
        lista.append(numero)
        numero = int(input("""Bienvenido al programa que encuentra el mayor 
            Teclea un número [-1 para salir]: """))
        print("El mayor es: ", max(lista))
    print("No hay valor mayor")




main()