# funciones de orden superior
# son aquellas funciones que reciben otra función como argumento

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# filter----------------------------------------------------------

lista_impares = [i for i in lista if i % 2 != 0]
#print(lista_impares)

# equivalente con filter
# filter(funcion anonima, iterable)
filter_impares = filter(lambda x: x % 2 != 0, lista)
# me retorna un iterable, por lo tanto lo convierto a lista
#print(list(filter_impares))

# map-------------------------------------------------------------

# filter(funcion anonima, iterable)
map_cuadrado = map(lambda x: x ** 2, lista)
# me retorna un iterable, por lo tanto lo convierto a lista
#print(list(map_cuadrado))


# reduce------------------------------------------------------------
from functools import reduce

all_mult = reduce(lambda x, y: x * y, lista)
print(all_mult)
