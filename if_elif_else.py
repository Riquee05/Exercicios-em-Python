#Exibe um Menu para interação do Usuario

menu = """

[m] Manha
[t] Tarde
[n] Noite

=> """

opcao = input(menu)

# Função If e Else para validar informações

if opcao == "m":
    print("Bom dia")

elif opcao == "t":
    print("Boa tarde")

elif opcao == "n":
    print("Boa noite")

else:
    print("Parametro Invalido")

