def calcular_resultado(P, Q, M):
    return (P and Q) or (not P and M)

def exibir_tabela_verdade():
    print("Tabela Verdade:")
    print("P | Q | M | R")
    print("--|---|---|---")
    for P in [True, False]:
        for Q in [True, False]:
            for M in [True, False]:
                R = calcular_resultado(P, Q, M)
                print(f"{'T' if P else 'F'} | {'T' if Q else 'F'} | {'T' if M else 'F'} | {'T' if R else 'F'}")
    print()

def obter_valor_entrada(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada == "!s":
            print("Funcionamento do programa foi interrompido, obrigado por usar.")
            exit()
        if entrada not in ["T", "F"]:
            print("Digite apenas 'T' ou 'F'. Para sair, digite '!s'.")
            continue
        return entrada == "T"

def main():
    exibir_tabela_verdade()
    
    while True:
        print("Para sair, digite '!s' ao ser solicitado.")
        
        P = obter_valor_entrada("Digite o valor de P (T ou F): ")
        Q = obter_valor_entrada("Digite o valor de Q (T ou F): ")
        M = obter_valor_entrada("Digite o valor de M (T ou F): ")

        R = calcular_resultado(P, Q, M)
        
        print("Resultado:")
        print(f"P: {'T' if P else 'F'} | Q: {'T' if Q else 'F'} | M: {'T' if M else 'F'} | R: {'T' if R else 'F'}")
        break 

if __name__ == "__main__":
    main()
