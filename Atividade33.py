Import.os
os.system ("cls")

arquivo = "texto.txt"

opcao = -1

while opcao != 0:

    print("\n0 - Sair")
    print("1 - Gravar linha")
    print("2 - Gravar linhas")
    print("3 - Exibir conteúdo")
    print("4 - Exibir uma linha")
    print("5 - Contar palavras")
    print("6 - Contar caracteres")
    print("7 - Contar palavras com N letras")
    print("8 - Contar uma palavra")
    print("9 - Finalizar processo")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        texto = input("Digite uma linha: ")

        arq = open(arquivo, "a")
        arq.write(texto + "\n")
        arq.close()

    elif opcao == 2:
        qtd = int(input("Quantas linhas? "))

        arq = open(arquivo, "a")

        for i in range(qtd):
            texto = input("Digite uma linha: ")
            arq.write(texto + "\n")

        arq.close()

    elif opcao == 3:
        arq = open(arquivo, "r")
        print(arq.read())
        arq.close()

    elif opcao == 4:
        linha = int(input("Digite a linha: "))

        arq = open(arquivo, "r")
        linhas = arq.readlines()

        if linha <= len(linhas):
            print(linhas[linha - 1])
        0
         else:
            print("Linha não existe")

        arq.close()

    elif opcao == 5:
        arq = open(arquivo, "r")
        texto = arq.read()
        arq.close()

        palavras = texto.split()
        print("Palavras:", len(palavras))

    elif opcao == 6:
        arq = open(arquivo, "r")
        texto = arq.read()
        arq.close()

        print("Caracteres:", len(texto))

    elif opcao == 7:
        n = int(input("Número de letras: "))

        arq = open(arquivo, "r")
        palavras = arq.read().split()
        arq.close()

        contador = 0

        for palavra in palavras:
            if len(palavra) == n:
                contador += 1

        print("Quantidade:", contador)

    elif opcao == 8:
        busca = input("Digite a palavra: ")

        arq = open(arquivo, "r")
        palavras = arq.read().split()
        arq.close()

        print("Quantidade:", palavras.count(busca))


    