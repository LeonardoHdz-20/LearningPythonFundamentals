print("Ejemplo del uso de colecciones tipo SET")

# Definir ejemplos con colecciones
first_collection = {1, 2, 3, 4, 5}
second_collection = {3, 4, 5, 6, 7, 8}

print("\nImpresión del contenido de la colección\n")
for item in first_collection:
    print(item)

union_set = first_collection.union(second_collection)
print(f"Unión de colecciones: {union_set}")

intersection_set = first_collection.intersection(second_collection)
print(f"Intersección de colecciones: {intersection_set}")

difference_set = first_collection.difference(second_collection)
print(f"Diferencia en colecciones: {difference_set}")

symmetric_difference_set = first_collection.symmetric_difference(second_collection)
print(f"Diferencia simétrica: {symmetric_difference_set}")

is_subset = first_collection.issubset(second_collection)
print(f"first_collection es subconjunto de second_collection: {is_subset}")

# Creando un nuevo conjunto con los cuadrados de los números del 1 al 9
cuadrados = {x**2 for x in range(10)}
print("Cuadrados:", cuadrados)
