#leonardo Job
        # 1 - Gravar linha  
        # 2 - Gravar linhas 
        # 3 - Exibir conteúdo 
        # 4 - Exibir uma linha 
        # 5 - Contar palavras  
        # 7 - Contar palavras com N letras 
        # 8 - Contar uma palavra

arquivo = "texto.txt"  # arquivo onde vai ficar salvo os textos

opcao = -1

# fica repetindo até o usuario escolher sair
while opcao != 0:

    print("\n0 - Sair")
    print("1 - Gravar linha")
    print("2 - Gravar linhas")
    print("3 - Exibir conteúdo")
    print("4 - Exibir uma linha")
    print("5 - Contar palavras")
    print("6 - Contar caracteres")
    print("7 - Contar palavras com X letras")
    print("8 - Contar uma palavra")

    opcao = int(input("Escolha: "))

            # 1 - Gravar linha
    if opcao == 1:
        texto = input("Digite uma linha: ")

        # Vai abre o arquivo e adiciona a linha no final
        with open(arquivo, "a") as arq:
            arq.write(texto + "\n")

                # 2 - Gravar linhas
    elif opcao == 2:
        qtd = int(input("Quantas linhas? "))

        # gravara varias linhas de uma vez
        with open(arquivo, "a") as arq:
            for i in range(qtd):
                texto = input("Digite uma linha: ")
                arq.write(texto + "\n")

        # 3 - Exibir conteúdo
    elif opcao == 3:

        # mostrara tudo que esta dentro do arquivo
        with open(arquivo, "r") as arq:
            print(arq.read())

        # 4 - Exibira uma linha
    elif opcao == 4:
        linha = int(input("Digite a linha: "))

        # pega todas as linhas do arquivo
        with open(arquivo, "r") as arq:
            linhas = arq.readlines()

        # verifica se a linha existe
        if 1 <= linha <= len(linhas):
            print(linhas[linha - 1])
        else:
            print("Linha não existe")

        # 5 - Contar palavras
    elif opcao == 5:
        with open(arquivo, "r") as arq:
            texto = arq.read()

        # separa o texto em palavras e conta elas
        palavras = texto.split()
        print("Palavras:", len(palavras))

        # 6 - Contar caracteres
    elif opcao == 6:
        with open(arquivo, "r") as arq:
            texto = arq.read()

        # conta todos os caracteres do arquivo
        print("Caracteres:", len(texto))

        # 7 - Contar palavras com X letras
    elif opcao == 7:
        X = int(input("Número de letras: "))

        with open(arquivo, "r") as arq:
            palavras = arq.read().split()

        contador = 0

        # verifica quais palavras tem o tamanho escolhido
        for palavra in palavras:
            if len(palavra) == X:
                contador += 1

        print("Quantidade:", contador)

    elif opcao == 8:
        # 8 - Contar uma palavra
        busca = input("Digite a palavra: ")

        with open(arquivo, "r") as arq:
            palavras = arq.read().split()

        # conta quantas vezes a palavra aparece
        print("Quantidade:", palavras.count(busca))





