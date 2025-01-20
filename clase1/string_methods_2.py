from operator import indexOf  # Aunque se importa, no se utiliza en este ejemplo.

message = "Los cuervos de la UTVT"

# len
size = len(message)

# replace
new_message = message.replace("", ",")

# find
index_of_u = message.find("u")

# split
message_sliced = message.split()

print(f"Tamaño de la cadena: {len(message)}")
print(f"Longitud de la cadena: {size}")
print(f"Nueva cadena: {new_message}")
print(f"Posición del elemento buscado: {index_of_u}")
print(f"Cadena particionada: {message_sliced}")
