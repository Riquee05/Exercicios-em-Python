


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
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def menu():

    while True:

        menu = """

Lista de Tarefas em Python
[1] Adicionar tarefa
[2] Remover Tarefa
[3] Listar Tarefa
[4] Sair

=> """
        opção = input(menu)

        if opção == "1":
            adicionar = input("Inserir Tarefa: ")
            adicionar_tarefas(adicionar)
        elif opção == "2":
            remover = input("Remover tarefa: ")
            remover_tarefas(remover)
        elif opção == "3":
            listar_tarefas()
        elif opção == "4":
            print("Sair")
            break
    
menu()