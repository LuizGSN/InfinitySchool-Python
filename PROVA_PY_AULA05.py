from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = list(map(lambda x: x ** 2, numeros))
print("Quadrados:", quadrados)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

soma = reduce(lambda x, y: x + y, numeros)
print("Soma:", soma)