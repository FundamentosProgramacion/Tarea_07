def calcularDivision(divisor, dividendo):
    cociente= 0
    sobrante=0
    while divisor >= dividendo:
        divisor = divisor - dividendo
        cociente+= 1

    return cociente











def main():
    divisor=int(input("Escribe el divisor:"))
    dividendo=int(input("Escribe el dividendo:"))

    print("La division de", divisor,"/",dividendo,"es:",calcularDivision(divisor,dividendo))



main()