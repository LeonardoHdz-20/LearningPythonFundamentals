print("Ejemplo con tuplas \n\n")

# Definición de una tupla
tupla_informacion = ('Ana PicaPiedra', 22, 95.5)
print(f"Información de la tupla: {tupla_informacion}")

# Desestructuración o unpacking
nombre_completo, edad, salario = tupla_informacion
print(f"Nombre: {nombre_completo}, Edad: {edad}, Salario: {salario}")

print("\n\nImpresión de la tupla con un ciclo FOR \n")
# Impresión de los elementos de una tupla
for item in tupla_informacion:
    print(item)
