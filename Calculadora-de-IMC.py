print("Bienvenido")

persona = {"Nombre":"", "Apellido":"", "Edad":0, "Peso":0, "Altura":0, "Direccion":"", "Telefono":""}

for j in persona:
	persona[j] = input(f"Ingrese su {j} :" )

imc = round(float(persona["Peso"])/(float(persona["Altura"])**2),2)
persona["IMC"] = imc

def cat_imc(imc):
	if imc < 18.5:
		print("Bajo Peso")
	elif imc < 24.9:
		print("uPeso Normal")
	elif imc < 29.9:
		print("Sobre Peso")
	elif imc < 34.9:
		print("Obesidad tipo I")
	elif imc < 39.9:
		print("Obesidad tipo II")
	elif imc < 40:
		print("Obesidad tipo III")

def imprimir(persona):
	for j in persona:
		print (j, ":", persona[j].upper())

cat_imc(imc)
imprimir(persona)