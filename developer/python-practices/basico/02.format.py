""" El format se usa para asignar variables dinamicamente """

saludo = 'Hola mundo'
altura = 1.60
edad = 20

#print("{}, kilos es mi peso.".format(edad)) 
# imprime en consola:
# 20, kilos es mi peso.

print("{}, años".format(edad))

my_string = "{}, mi edad es {} y mido {}"

# tambien es posible texto dentod de los corchetes usando la funcion format
print(my_string.format("hola mundo", "33", "1.60")) 
# imprime en consola:
# hola mundo, mi edad es 33 y mido 1.60

