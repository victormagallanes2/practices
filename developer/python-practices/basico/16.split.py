# La funcion split se usa para cortar o extraer cadena de caracteres

# supiniendo que quiero generar un usuario unico tomando como base
# el correo de un usuario

email = "victormagallanes2@gmail.com"

# si quiero tomar solo lo que esta antes del @ entonces uso split
# para separa las secciones antes y depues del @. Por defecto split
# me genera una lista con ambos valores

x = email.split("@")
print(x)
# esto imprimiria esta lista ['victormagallanes2', 'gmail.com']

# entonces tomo el valor que necesito de la lista y le agrago un serial
# aleatorio usando el modulo random
import random
y = random.randrange(0, 99999, 4)
print(str(x[0])+str(y))
# esto imprimiria algo como victormagallanes283488

