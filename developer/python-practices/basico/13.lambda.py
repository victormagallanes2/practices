"""Las lambda son parecidas a las funciones, las cuales generalmente,
   se utilizan para tareas cortas o de un solo uso, estas funciones
   lambda no necesitan tener nombre"""

# supongamos que tenemos esta funcion

def suma(a, b):
	return(a + b)

# su equivalente usando lambda seria

s = lambda a, b: a + b
print(s(5, 2))

# tambien se le puede pasar diccionarios, listas y tuplas como parametros
planets = [
    ("jupiter", 5612, 0.26, 65),
    ("mercury", 600, 12, 84),
    ("eart", 800, 120, 20)
    ]

size = lambda planet: planet[1]

planets.sort(key=size, reverse=True)
print(planets)