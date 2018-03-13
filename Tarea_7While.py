#Autor: Eduardo Roberto Müller Romero, A01745219

def Divisores(dividendo, divisor):
	a = dividendo - divisor
	contador = 1
	while a >= divisor:
		a = a - divisor
		contador += 1
	residuo = a
	return contador, residuo

def elMayor():
	valores = []
	valor = int()
	while valor != -1:
		valor = int(input("Valor: "))
		valores.append(valor)
	el_mayor = max(valores)
	return el_mayor

def main():
	user = int()
	while user != 3:
		print("Opciones\n1. Divisores\n2. Mayor\n3. Salir")
		user = int(input("Selecciona una opción: "))
		if user == 1:
			print()
			x = int(input("Dividendo: "))
			y = int(input("Divisor: "))
			cociente, residuo = Divisores(x, y)
			if residuo == 0:
				print(x, "/", y, "es igual a", cociente, "y es exacta (no hay residuo)")
			else:
				print(x, "/", y, "es igual a", cociente, "con un residuo de", residuo)
		elif user == 2:
			high = elMayor()
			print("De todos los valores dados", high, "es el mayor")
		elif user != (1 and 2 and 3):
			print("Opción NO Válida")
	print("FIN DE LA TRANSMISIÖN")

main()