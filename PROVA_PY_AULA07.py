def AdicionarAluno(alunos):
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    if matricula in alunos:
        print(f"Aluno com matrícula {matricula} já existe.")
    else:
        alunos[matricula] = nome
        print(f"Aluno {nome} com matrícula {matricula} adicionado com sucesso.")

def RemoverAluno(alunos):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print(f"Aluno com matrícula {matricula} removido com sucesso.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")

def AtualizarAluno(alunos):
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        nome = input(f"Digite o novo nome para o aluno com matrícula {matricula}: ")
        alunos[matricula] = nome
        print(f"Nome do aluno com matrícula {matricula} atualizado para {nome}.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")

def VerAlunos(alunos):
    if alunos:
        print("\nLista de Alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado.")

def main():
    alunos = {}
    while True:
        print("\n1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            AdicionarAluno(alunos)
        elif opcao == '2':
            RemoverAluno(alunos)
        elif opcao == '3':
            AtualizarAluno(alunos)
        elif opcao == '4':
            VerAlunos(alunos)
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
