# Entrada de datos mediante la consola INPUT

name = input("¿Cuál es tu nombre? ")
age = int(input("¿Cuál es tu edad? "))
salary = float(input("¿Cuál es tu salario? "))
total_pets = eval(input("¿Cuantas mascotas tienes? "))
university = input("¿Cuál es el nombre de tu universidad? ")

print(f"Hola, me llamo {name}, mi edad es {age} y mi universidad es {university}")
print(type(name))
print(type(age))
print(type(salary))
print(type(total_pets))

