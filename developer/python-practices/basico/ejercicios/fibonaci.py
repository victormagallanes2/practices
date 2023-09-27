# Es una ecuacion matematica que expresa una espiral Fn = Fn-2 + Fn-1

# crear una funcion que represente la secuenci fibonaci dado un rango numerico

# opcion 1

# def fibonaci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return fibonaci(n-1) + fibonaci(n-2)

# for n in range(1, 11):
#     print(n, ":", fibonaci(n))

"""1:1
2:1
para el 3
se ejecuta fibonaci(3-1) que es 2 y la funcion se ejecuta con
valor n = 2 dando como resultado 1
tambien se ejecuta fibonaci(3-2) que es 1 dando como resultado n = 1
entonces 1 + 1 = 2 para el valor de n = 3
3:2
asi va el orden de ejecuta.
esta funcion es ineficiente ya que tiene que ejecutarse asi misma muchas
veces asi misma creando un retardo cada vez mas grande a medida que el
numero se va haciendo mas grande por ejemplo si colocamos rangos de miles"""

"""Para resolver este problema es posible guardar el resultado de n
   en un diccionario para que cuando se ejecute la funcion no tenga
   que volver a hacer el calculo sino que se extraiga de la cache"""

# opcion 2

fibonaci_cache = {}

def fibonaci(n):
    if n in fibonaci_cache:
        return fibonaci_cache[n]
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        value = fibonaci(n-1) + fibonaci(n-2)
    fibonaci_cache[n] = value
    return value

for n in range(1, 11):
    print(n, ":", fibonaci(n))

