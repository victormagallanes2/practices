"""la funcion map se usa para realizar varios calculos en donde se tiene
   lista de valores como parametros"""

import math

# suponiendo que se necesite calcular el area de un circulo dado un radio

def area(r):
    return math.pi * (r**2)

# esta funcion cumple el requisito pero como se haria si tenemos muchos
# radios que calcular? podriamos hacer esto:

areas = []
redios = [ 2, 4, 6, 8]

for r in redios:
    a = area(r)
    areas.append(a)

print(areas)

# pero tambien podriamos utilizar map

x = list(map(area, redii))
print(x)

# tambien es posible usar lambda y map combinados

y = list(map(lambda r: math.pi * (r**2), redii))
print(y)