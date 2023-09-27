# Fibonacci:

#     Escribe una función que genere los primeros 'n' números de
# la secuencia de Fibonacci.



def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
for x in range(10):
    print(fib(x))


#print(fib(8))