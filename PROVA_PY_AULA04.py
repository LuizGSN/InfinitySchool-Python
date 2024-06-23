def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Parabéns, sua média é 10"
    else:
        return "Aprovado"

def main():
    notas = []
    print("Digite as notas dos alunos. Digite 'q' para sair e calcular a média.")
    
    while True:
        entrada = input("Digite uma nota: ")
        if entrada.lower() == 'q':
            break
        try:
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print("Por favor, digite uma nota entre 0 e 10.")
            else:
                notas.append(nota)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    if notas:
        media = calcular_media(notas)
        situacao = verificar_situacao(media)
        print(f"A média do aluno é: {media:.2f}")
        print(f"Situação: {situacao}")
    else:
        print("Nenhuma nota foi inserida.")

if __name__ == "__main__":
    main()
