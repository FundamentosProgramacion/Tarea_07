#Jossian Abimelec García Quijano


def dividir(dividendo,divisor):
    contador=0
    operacion=dividendo
    while operacion>=divisor:
        operacion=operacion-divisor
        contador+=1
    print(dividendo,"/",divisor,"=",contador,", sobra",operacion)


def main():
    dividir(15, 6)
    dividir(5, 6)
    dividir(500, 21)
    dividir(151, 32)
    dividir(1024, 8)

    
main()