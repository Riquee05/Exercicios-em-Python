class produto:
    def __init__(self, nome , preço , estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

        return f"Itens em Estoque: Produto {self.nome} | preço {self.preço} | Itens em estoque {self.estoque}"

class estoque:

    def __init__(self):
        self.itens_estoque = []

    def registrar_estoque(self, nome , preço , estoque):
        if any(item.nome == nome for item in self.itens_estoque):
            print(f"Erro: Item ja existente -  {nome}.")
            return
        item = produto(self , nome , preço , estoque)
        self.itens_estoque.append(item)
        print(f"Item {nome} Registrado com Sucesso")

    def visualizar_itens(self):
        if self.itens_estoque:
            print("Todos os itens ordenados")
            for item in sorted(self.itens_estoque):
                print(item)

def menu():
    gerencia = produto()

    while True:
        print("\n Sistema Estoque Geral")
        
    