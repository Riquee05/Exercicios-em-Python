class Funcionario:

    def __init__(self, nome, salario, cargo): # Bloco Construtor da Classe Funcionario
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        

    def calculo_imposto(self): # Definição de função para Calculo de imposto sobre Salario
        if self.salario <= 2000:
            imposto = 0
        elif self.salario <= 3000:
            imposto = 7.5
        elif self.salario <= 4000:
            imposto = 15.0
        elif self.salario <= 5000:
            imposto = 22.5
        else:
            imposto = 27.5
        
        return self.salario * imposto / 100

    def __str__(self): # Definindo uma Função para retornar em String(Texto)
        imposto = self.calculo_imposto()
        salario_liquido = self.salario - imposto
        return (f"Colaborador - {self.nome}, cargo - {self.cargo}, "
                f"salario bruto - {self.salario}, imposto - {imposto:.2f}, "
                f"salario liquido - {salario_liquido:.2f}")
    
# O f" antes do texto quer dizer que iremos colocar valores ou variaveis dentro do texto;
# dentro das chaves{} temos as variaveis que iremos ultililzar e o :.2f Ira transformar o texto em um numero
# Float com duas casas decimais Exemplo 3700.00 os dois zeros depois de 3700 e o que faz o :.2f

funcionario1 = Funcionario("Henrique Oliveira", 3700.00, "Desenvolvedor Backend Junior")
funcionario2 = Funcionario("Pedro Henrique", 4200.00, "Analista de Almoxarifado")
funcionario3 = Funcionario("Gabriel Anacleto", 2900.00, "Estagiario")

print(funcionario1)
print(funcionario2)
print(funcionario3)