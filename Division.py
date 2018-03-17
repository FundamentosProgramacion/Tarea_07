def calcularDivisiones(dividendo, divisor):
    cociente=0
    while divisor<=dividendo:
        cociente+=0
        division=dividendo-divisor
        if cociente>divisor:
            cociente-=cociente-divisor
        return cociente







def main():

    print(calcularDivisiones(15,6))



main()