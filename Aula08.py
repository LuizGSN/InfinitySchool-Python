# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR 5 NÚMEROS, GUARDE OS NÚMEROS EM UMA LISTA
# QUANDO TERMINAR DE INSERIR, PERCORRA A LISTA QUE FOI PREENCHIDA E DESCUBRA QUAL O MAIOR NÚMERO DA LISTA

lista_de_numeros = []

for i in range(1,6):
    numero = float(input(f"Digite o {i}º número: "))
    lista_de_numeros.append(numero)


maior_numero = lista_de_numeros[0]

for numero_da_vez in lista_de_numeros:
    if numero_da_vez > maior_numero:
        maior_numero = numero_da_vez


print(f"O maior número foi o {maior_numero}")






# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO CADASTRAR UM NÚMERO ILIMITADO 
# DE FRUTAS E GUARDE ELAS EM UMA LISTA DE FRUTAS DEPOIS PERGUNTE PARA O 
# USUÁRIO QUAL FRUTA ELE DESEJA REMOVER, E REMOVA AQUELA FRUTA DA LISTA CASO ELA EXISTA, 
# CASO NÃO MOSTRE UMA MENSAGEM DE ERRO.




lista_de_frutas = []

while True:
    fruta = str(input("Digite o nome de uma fruta ou 'sair': ")).strip()
    if fruta.lower() == "sair":
        break
    else:
        lista_de_frutas.append(fruta)
    
fruta_excluida = str(input("Digite o nome da fruta que você quer excluir: ")).strip()

fruta_encontrada = False

for fruta_da_vez in lista_de_frutas:
    if fruta_da_vez.lower() == fruta_excluida.lower():
        lista_de_frutas.remove(fruta_da_vez)
        fruta_encontrada = True
        print("Fruta removida com sucesso")

if fruta_encontrada == False:
    print("Fruta não encontrada")


for fruta_da_vez in lista_de_frutas:
    print(fruta_da_vez)






# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO CADASTRAR UM NÚMERO ILIMITADO DE FRUTAS EM UM ESTOQUE, 
# PASSANDO O NOME DA FRUTA, PREÇO E QUANTIDADE EM ESTOQUE E ENTÃO GUARDE ELAS EM UMA LISTA DE FRUTAS 
# DEPOIS PERGUNTE PARA O USUÁRIO QUAL FRUTA ELE DESEJA REMOVER, 
# E REMOVA AQUELA FRUTA DA LISTA CASO ELA EXISTA, CASO NÃO MOSTRE UMA MENSAGEM DE ERRO.


lista_de_frutas = []

while True:
    nome_da_fruta = str(input("Digite o nome de uma fruta ou 'sair': ")).strip()
    if nome_da_fruta.lower() == "sair":
        break
    else:
        preco_da_fruta = float(input("Digite o preço da fruta: "))
        qtde_da_fruta = int(input("Digite a quantidade de frutas no estoque: "))

        fruta = {
            "Nome": nome_da_fruta,
            "Preço": preco_da_fruta,
            "Quantidade": qtde_da_fruta
        }

        lista_de_frutas.append(fruta)
    
fruta_excluida = str(input("Digite o nome da fruta que você quer excluir: ")).strip()

fruta_encontrada = False

for fruta_da_vez in lista_de_frutas:
    if fruta_da_vez["Nome"].lower() == fruta_excluida.lower():
        lista_de_frutas.remove(fruta_da_vez)
        fruta_encontrada = True
        print("Fruta removida com sucesso")

if fruta_encontrada == False:
    print("Fruta não encontrada")


for fruta_da_vez in lista_de_frutas:
    print(f"""
    Informações da Fruta:
    Nome -> {fruta_da_vez["Nome"]}
    Preço -> {fruta_da_vez["Preço"]}
    Quantidade no estoque -> {fruta_da_vez["Quantidade"]}
""")