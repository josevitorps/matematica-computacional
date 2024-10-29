def obter_valor_float(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada == "!s":
            print("Funcionamento do programa foi interrompido, obrigado por usar.")
            exit()
        try:
            return float(entrada)
        except ValueError:
            print("Digite apenas número.")

def bissetriz_interna(lado1, lado2, lado3):
    return lado2 / (lado1 + lado2)

def bissetriz_externa(lado1, lado2, lado3):
    return lado2 / (lado1 - lado2)

def main():
    while True:
        criterio = input("Digite qual bissetriz você deseja verificar (interna, externa) ou '!s' para sair: ").lower()
        if criterio == "!s":
            print("Funcionamento do programa foi interrompido, obrigado por usar.")
            return
        elif criterio in ["interna", "externa"]:
            lado1 = obter_valor_float("Digite o lado 1: ")
            lado2 = obter_valor_float("Digite o lado 2: ")
            lado3 = obter_valor_float("Digite o lado 3: ")
            if criterio == "interna":
                resultado = bissetriz_interna(lado1, lado2, lado3)
                print(f"Resultado da Bissetriz Interna: {resultado}")
                break  # Finaliza após apresentar o resultado
            elif criterio == "externa":
                if lado1 - lado2 == 0:
                    print("Erro: Divisão por zero na bissetriz externa.")
                else:
                    resultado = bissetriz_externa(lado1, lado2, lado3)
                    print(f"Resultado da Bissetriz Externa: {resultado}")
                break  # Finaliza após apresentar o resultado
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
