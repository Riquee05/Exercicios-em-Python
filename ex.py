import datetime


tarefas = []

def adicionar_tarefas(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa Adicionada com Sucesso {tarefas}")

def remover_tarefas(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa removida com Sucesso {tarefas}")
    else:
        print("Tarefa Não encontrada")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista")
    else:
        print("Lista de tarefas")
        for i in enumerate(tarefas, 1):
            print(f"{i}. {tarefas}")

def menu():

    while True:

        menu = """

Lista de Tarefas em Python
[1] Adicionar tarefa
[2] Remover Tarefa
[3] Listar Tarefa

"""
        opção = input(menu)

        if opção == "1":
            adicionar = input("Inserir Tarefa(Numero , tarefa)")
            adicionar_tarefas
        elif opção == "2":
            remover = input("Remover tarefa ")
            remover_tarefas
        elif opção == "3":
            print("Lista de Tarefas ")
            listar_tarefas()
        break
    else:
        print("Opção Invalida, tente novamente")
    
menu()