n = [[], []]
valor = 0
contador_p = 0
contador_i = 0
soma = 0

for i in range(1, 11):
    valor = int(input(f'Digite o {i}o. valor:'))
    soma += valor
    if valor % 2 == 0:
        n[0].append(valor)
        contador_p += 1
    else:
        n[1].append(valor)
        contador_i += 1
        
print('-='* 50)
n[0].sort()
n[1].sort()
print(f"Os números pares digitados foram: {n[0]} e o total de números pares são: {contador_p}")
print(f"Os números ímpares digitados foram: {n[1]} e o total de números ímpares são: {contador_i}")
print (f"A soma total de todos os números pares e ímpares da: {soma}")