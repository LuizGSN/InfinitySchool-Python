def adicionar_produto(lista_produtos, total_produtos):
    produto = input("Nome do produto: ")
    valor = float(input("Valor unitário do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    total = valor * quantidade
    lista_produtos.append({"produto": produto, "valor": valor, "quantidade": quantidade, "total": total})
    total_produtos += total
    return total_produtos

def ver_lista_produtos(lista_produtos, total_produtos):
    print("\nLista de Produtos:")
    for p in lista_produtos:
        print(f"Produto: {p['produto']}, Valor Unitário: {p['valor']:.2f}, Quantidade: {p['quantidade']}, Total: {p['total']:.2f}")
    print(f"\nValor Total de Todos os Produtos: {total_produtos:.2f}\n")

def atualizar_produto(lista_produtos, total_produtos):
    nome_produto = input("Nome do produto a ser atualizado: ")
    for p in lista_produtos:
        if p['produto'] == nome_produto:
            total_produtos -= p['total']
            p['produto'] = input("Novo nome do produto: ")
            p['valor'] = float(input("Novo valor unitário do produto: "))
            p['quantidade'] = int(input("Nova quantidade do produto: "))
            p['total'] = p['valor'] * p['quantidade']
            total_produtos += p['total']
            return total_produtos
    print("Produto não encontrado!")
    return total_produtos

def remover_produto(lista_produtos, total_produtos):
    nome_produto = input("Nome do produto a ser removido: ")
    for p in lista_produtos:
        if p['produto'] == nome_produto:
            total_produtos -= p['total']
            lista_produtos.remove(p)
            return total_produtos
    print("Produto não encontrado!")
    return total_produtos

def main():
    lista_produtos = []
    total_produtos = 0.0

    while True:
        print("1. Adicionar produto")
        print("2. Ver lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            total_produtos = adicionar_produto(lista_produtos, total_produtos)
        elif opcao == 2:
            ver_lista_produtos(lista_produtos, total_produtos)
        elif opcao == 3:
            total_produtos = atualizar_produto(lista_produtos, total_produtos)
        elif opcao == 4:
            total_produtos = remover_produto(lista_produtos, total_produtos)
        elif opcao == 5:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
