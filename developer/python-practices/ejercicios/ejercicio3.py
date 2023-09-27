# Inversión de cadena:

#     Escribe una función que tome una cadena como entrada
# y devuelva la cadena invertida. Por ejemplo, si la entrada es"Hola",
# la función debe devolver "aloH".


def invertir(cadena):
    x = cadena[::-1]
    return x

print(invertir("hola"))