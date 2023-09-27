# Suma de elementos en una lista:

#     Escribe una función que tome una lista de números como entrada y
# devuelva la suma de todos los elementos de la lista.

lista = [1, 2, 3, 4, 5]

def suma(lista):
    return sum(lista)

print(suma(lista))


lista1 = [1, 2, 3, 4, 5]

def suman(lista1):
    sumatoria = 0
    for x in lista1:
        sumatoria += x
    return(sumatoria)

print(suman(lista1))