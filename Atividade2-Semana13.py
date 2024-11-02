def calcular_idades():
    resultados = []

    while True:
        try:
            entrada1 = input("Digite a idade do primeiro homem ou !s para sair: ")
            if entrada1.lower() == '!s':
                return
            
            if not entrada1.isdigit():
                print("Erro: Insira um número inteiro válido.")
                continue
            homem1 = int(entrada1)

            entrada2 = input("Digite a idade do segundo homem ou !s para sair: ")
            if entrada2.lower() == '!s':
                return

            if not entrada2.isdigit():
                print("Erro: Insira um número inteiro válido.")
                continue
            homem2 = int(entrada2)

            entrada3 = input("Digite a idade da primeira mulher ou !s para sair: ")
            if entrada3.lower() == '!s':
                return

            if not entrada3.isdigit():
                print("Erro: Insira um número inteiro válido.")
                continue
            mulher1 = int(entrada3)

            entrada4 = input("Digite a idade da segunda mulher ou !s para sair: ")
            if entrada4.lower() == '!s':
                return

            if not entrada4.isdigit():
                print("Erro: Insira um número inteiro válido.")
                continue
            mulher2 = int(entrada4)

            if homem1 < 0 or homem2 < 0 or mulher1 < 0 or mulher2 < 0:
                print("Por favor, digite idades positivas.")
                continue

            homem_mais_velho = max(homem1, homem2)
            homem_mais_novo = min(homem1, homem2)
            mulher_mais_velha = max(mulher1, mulher2)
            mulher_mais_nova = min(mulher1, mulher2)

            soma = homem_mais_velho + mulher_mais_nova
            produto = homem_mais_novo * mulher_mais_velha

            resultados.append((homem_mais_velho, mulher_mais_nova, soma, homem_mais_novo, mulher_mais_velha, produto))

            print(f"Soma da idade do homem mais velho com a mulher mais nova: {soma}")
            print(f"Produto da idade do homem mais novo com a mulher mais velha: {produto}")

            break 

        except ValueError:
            print("Erro: Insira apenas números inteiros.")
            continue

    print("\nTabela Verdade - Resultados:")
    print("Mais Velho (Homem) | Mais Nova (Mulher) | Soma | Mais Novo (Homem) | Mais Velha (Mulher) | Produto")
    for resultado in resultados:
        print(f"{resultado[0]:<18} | {resultado[1]:<16} | {resultado[2]:<5} | {resultado[3]:<16} | {resultado[4]:<17} | {resultado[5]}")

calcular_idades()
