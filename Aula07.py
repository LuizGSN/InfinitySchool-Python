def contar_vogais(palavra:str) -> int:
    vogais = "aeiouáàãâéêíóôõú"
    contador = 0
    for letra_atual in palavra.lower():
        if letra_atual in vogais:
            contador += 1
    return contador

def contar_consoantes(palavra:str) -> int:
    consoates = "bcdfghjklmnpqrstvxywz"
    contador = 0
    for letra_atual in palavra.lower():
        if letra_atual in consoates:
            contador += 1
    return contador


def contar_palavras(texto:str) -> int:
    contador = 1
    for caracter_atual in texto.lower().strip():
        if caracter_atual == " ":
            contador += 1
    return contador


def contar_pontuacoes(texto:str) -> int:
    pontos = ".,;!?:"
    contador = 0
    for caracter_atual in texto:
        if caracter_atual in pontos:
            contador += 1
    return contador



# 1 - FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INDETERMINADO DE NÚMEROS E RETORNE QUAL O MAIOR ENTRE ELES
# 2 - FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INDETERMINADO DE NÚMEROS E RETORNE QUAL O MENOR ENTRE ELES
# 3 - FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INDETERMINADO DE NÚMEROS E RETORNE QUAL A MÉDIA DELES
# 4 - FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INDETERMINADO DE NÚMEROS E RETORNE QUAL A SOMA DELES



def maior_numero(*numeros:list) -> float:
    maior = numeros[0]
    for numero_atual in numeros:
        if numero_atual > maior:
            maior = numero_atual
    return maior


def menor_numero(*numeros:list) -> float:
    menor = numeros[0]
    for numero_atual in numeros:
        if numero_atual < menor:
            menor = numero_atual
    return menor


def media_dos_numeros(*numeros:list) -> float:
    soma = 0
    for numero_atual in numeros:
       soma += numero_atual
    media = soma / len(numeros)
    return media

def soma_dos_numeros(*numeros:list) -> float:
    soma = 0
    for numero_atual in numeros:
       soma += numero_atual
    return soma


import texto

palavra_digitada = str(input("Digite uma palavra: "))


print(f"A palavra {palavra_digitada} possui {texto.contar_vogais(palavra=palavra_digitada)} vogais")

print(f"A palavra {palavra_digitada} possui {texto.contar_consoantes(palavra=palavra_digitada)} cosoantes")





from texto import contar_vogais, contar_consoantes

palavra_digitada = str(input("Digite uma palavra: "))


print(f"A palavra {palavra_digitada} possui {contar_vogais(palavra=palavra_digitada)} vogais")

print(f"A palavra {palavra_digitada} possui {contar_consoantes(palavra=palavra_digitada)} cosoantes")




from matematica.numeros import *


print(maior_numero(5,6,15,27,35,4,2,80))



# ATIVIDADE 1
from operacoes import *

while True:
    menu = int(input("""
    Escolha uma opção
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
"""))
    if(menu == 0):
        print("Fim do programa")
        break
    
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    match menu:
        case 1:
            print(somar(n1=numero1, n2=numero2))
        case 2:
            print(subtrair(n1=numero1, n2=numero2))
        case 3:
            print(multiplicar(n1=numero1, n2=numero2))
        case 4:
            print(dividir(n1=numero1, n2=numero2))
        case _:
            print("Opção Inválida")

