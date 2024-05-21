menu = """
Bem vindo ao Bebidas Online
Escolha sua opção

[1]. Agua
[2]. Refrigerante
[3]. Agua de Coco
[4]. Suco de Fruta(Lata)

Insira sua resposta => """



opcao = input(menu)

agua = 2.00
refrigerante = 6.00
aguacoco = 5.00
sucolata = 3.50


if opcao == "1":
    print("\n Voce Selecionou Agua")
    print("Valor R$" , agua)
    

elif opcao == "2":
    print("Voce Selecionou Rerigerante")
    print("Valor R$" , refrigerante)


elif opcao == "3":
    print("Voce Selecionou Agua")
    print(" Valor R$" , aguacoco)


elif opcao == "4":
    print("Voce Selecionou Suco de Fruta(Lata)")
    print("Valor R$" , sucolata)



pagamento = """
Escolha seu Metodo de Pagamento

[d]. Dinheiro
[c]. Cartões Debito ou Credito
[p]. PIX

Insira sua resposta => """

pgto = input(pagamento)

if pgto == "d":
    dinheiro = input("Insira a Cedula no Local Indicado")
    dinheiro = input("Validando Pagamento")
    dinheiro = input("Compra efetuada com Sucesso")

elif pgto == "c":
    print("Insira seu Cartão")
    cartao = input("\n [1] Debito" "\n [2] Credito" "\n" )
    cartao = input ("Insira sua Senha")
    cartao = input ("Iprimindo Comprovante de Pagamento")
    print("Compra efetuada com Sucesso")

elif pgto == "p":
    pix = input ("Gerando Codigo PIX")
    pix  = input("Aguardando Pagamento")
    pix = input ("Compra efetuada com Sucesso")


    