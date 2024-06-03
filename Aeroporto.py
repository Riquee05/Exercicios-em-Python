from datetime import datetime

class Voo:
    def __init__(self, numero, companhia, destino, hora_partida):
        self.numero = numero
        self.companhia = companhia
        self.destino = destino
        self.hora_partida = datetime.strptime(hora_partida, "%H:%M")

    def __str__(self):
        return f"Voo {self.numero} | Companhia: {self.companhia} | Destino: {self.destino} | Hora de Partida: {self.hora_partida.strftime('%H:%M')}"

class Aeroporto:
    def __init__(self):
        self.voos = []

    def registrar_voo(self, numero, companhia, destino, hora_partida):
        if any(voo.numero == numero for voo in self.voos):
            print(f"Erro: Já existe um voo com o número {numero}.")
            return
        voo = Voo(numero, companhia, destino, hora_partida)
        self.voos.append(voo)
        print(f"Voo {numero} registrado com sucesso!")

    def consultar_voos_por_destino(self, destino):
        voos_destino = [voo for voo in self.voos if voo.destino == destino]
        if voos_destino:
            print(f"Voos para {destino}:")
            for voo in voos_destino:
                print(voo)
        else:
            print(f"Não há voos registrados para o destino {destino}.")

    def visualizar_todos_os_voos(self):
        if self.voos:
            print("Todos os voos registrados (ordenados por hora de partida):")
            for voo in sorted(self.voos, key=lambda x: x.hora_partida):
                print(voo)
        else:
            print("Não há voos registrados.")

def menu():
    aeroporto = Aeroporto()
    while True:
        print("\nSistema de Gerenciamento de Voos")
        print("1. Registrar Voo")
        print("2. Consultar Voos por Destino")
        print("3. Visualizar Todos os Voos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = input("Número do voo: ")
            companhia = input("Companhia aérea: ")
            destino = input("Destino: ")
            hora_partida = input("Hora de partida (HH:MM): ")
            aeroporto.registrar_voo(numero, companhia, destino, hora_partida)
        elif opcao == "2":
            destino = input("Destino: ")
            aeroporto.consultar_voos_por_destino(destino)
        elif opcao == "3":
            aeroporto.visualizar_todos_os_voos()
        elif opcao == "4":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
