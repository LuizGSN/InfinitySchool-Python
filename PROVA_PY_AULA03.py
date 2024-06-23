def menu():
    continuar=1

    while continuar:
        continuar = int(
            input("0. Sair\n"+
                  "1. Exibir lista de alunos com sua matricula (cada aluno tem uma matricula)\n"+
                  "2. Inserir aluno e matricula\n"+
                  "3. Alterar a matricula de um aluno\n"+
                  "4. Consultar matricula de um aluno específico\n"+
                  "5. Apagar um aluno da lista\n"))
        if continuar==1:
            exibir()
        elif continuar == 2:
            inserir()
        elif continuar == 3:
            alterar()
        elif continuar == 4:
            consultar()
        elif continuar == 5:
            apagar()
        elif continuar == 0:
            print("Encerrando programa")
        else:
            print("Opção inválida")
        
def exibir():
    for nome in alunos.keys():
        print("Nome: ", nome, " - Matricula: ", alunos[nome])
        
def inserir():
    nome = input("Digite o nome do aluno: ")
    matricula = float(input("Matricula dele: "))

    if alunos.get(nome):
        print("Ja existe o aluno ",nome)
    else:
        alunos[nome] = matricula
    
def alterar():
    nome = input("Aluno a mudar a matricula: ")
    matricula = float(input("Nova Matricula     : "))

    if nome in alunos.keys():
        alunos[nome] = matricula
    else:
        print("Não existe esse aluno")
        
def consultar():
    nome = input("Digite o nome do aluno: ")

    if alunos.get(nome):
        print("Nota de ",nome, ": ", alunos[nome])
    else:
        print("Nao existe tal aluno")
    
def apagar():
    nome = input("Apagar que aluno: ")

    if alunos.get(nome):
        alunos.pop(nome)
    else:
        print("Não existe o aluno ",nome)
        
alunos = {}
menu()