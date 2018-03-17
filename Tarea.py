#Autor Karla Fabiola Ramirez Martinez
#Tarea division y maximo

#Es la funcion que hace la division! :D

def division():
    print("Estas en el programa para dividir!")
    divisor=0
    dividendo=0
    x=int(input("Dime el divisor!: "))
    divisor+=x
    y=int(input("Dime el dividendo!: "))
    dividendo+=y
    div=dividendo
    divoriginal=divisor
    dividir=0
    while divisor>=div:
        divisor=divisor-div
        if divisor==div:
            divisor=0

        dividir+=1

    resultado=print(divoriginal," / ",div," = ",dividir," y sobran",divisor)

#Funcion que calcula el mazimo utilizando listas
def maximo():
    print("Hola teclea los numeros que desees y te dire el mayor!")
    lista=[]
    x=int(input("Muy bien dime el valor (si quieres acabar solo necesitas poner -1): "))
    while x!=-1:
        lista.append(x)
        x=int(input("Muy bien dime el valor (si quieres acabar solo necesitas poner -1): "))

    mayor=max(lista)
    print("El mayor es: ",mayor)


#Funcion principalñ
def main():
    print("Menu!\n1)Division\n2)Encontrar maximo\n0)Salir")
    opcion = int(input("¿Que deseas Hacer? "))
    while opcion!=0:
        if opcion == 1:
            division()
        elif opcion == 2:
            maximo()
        opcion = int(input("¿Que deseas Hacer? "))
    print("¡ Gracias ! Espero haya sido de utilidad")


main()