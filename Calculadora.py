numero1 = float(input("Insira o Primeiro Numero "))

menu = """
===Escolha a Operação===

[+]. Soma
[-]. Subtração
[*]. Multiplicação
[/]. Divisão 


=> """

numero2 = float(input("Insira o Segundo Numero "))

opcao = input(menu)

while True:
    if opcao == "+":
        resultado = numero1 + numero2
    elif opcao == "-":
        resultado = numero1 - numero2
    elif opcao == "*":
        resultado = numero1 * numero2
    elif opcao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
    else:
        print("Operação Invalida, tente novamente ")
            
        

    print(f"\n Resultado de {numero1} {opcao} {numero2} = {resultado}")
    break