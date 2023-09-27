"""La funcion filter se usa para filtrar cosas"""


# teniendo una lista de paises

latinamerica = ["", "colombia", "venezuela", "","panama", "brazil"]

# se puede usar filter para filtrar los espacios vacios

paises = list(filter(None, latinamerica))
print(paises)

# suponiendo que se quiere tomar solo los elementos divisibles entre 2
# de esta lista

nums = [0, 2, 5, 8, 10, 23, 31, 35, 36, 47, 50, 77, 93]

# podriamos usar esta funcion
result = []
def operacion(x):
    for n_div in x:
        if n_div % 2 == 0:
            result.append(n_div)
    print(result)
    return result
        
operacion(nums)

# podriamos usar filter y lambda combinados

result = filter(lambda x: x % 2 == 0, nums)
print(result)


