def imprimir_tabela_verdade():
    print("Tabela Verdade para Cálculo do Salário:")
    print("Casos | num_carros > 0 | num_carros > 10 | Salário Fixo | Comissão por Carro | 5% sobre Total de Vendas | Bônus (10% sobre Total de Vendas)")
    print("1     | Sim            | Não            | Sim          | Sim                | Sim                       | Não")
    print("2     | Não            | Não            | Sim          | Não                | Não                       | Não")
    print("3     | Sim            | Sim            | Sim          | Sim                | Sim                       | Sim")
    print("------------------------------------------------------------------------------")

def calcular_salario(salario_base, comissao, carros_vendidos, total_vendas):
    salario = salario_base
    if carros_vendidos > 0:
        salario += comissao * carros_vendidos
        salario += 0.05 * total_vendas
        if carros_vendidos > 10:
            salario += 0.10 * total_vendas
    return salario

def solicitar_entrada(mensagem, tipo=float):
    while True:
        entrada = input(mensagem)
        if entrada == "!s":
            print("Programa encerrado.")
            exit()
        elif entrada == "!r":
            print("Reiniciando o programa...\n")
            main()
            return None
        try:
            return tipo(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def main():
    imprimir_tabela_verdade()

    salario_base = solicitar_entrada("Digite o salário fixo do vendedor: R$ ")
    comissao = solicitar_entrada("Digite a comissão fixa por carro vendido: R$ ")
    carros_vendidos = solicitar_entrada("Digite o número de carros vendidos: ", int)
    total_vendas = solicitar_entrada("Digite o valor total das vendas: R$ ")

    salario_final = calcular_salario(salario_base, comissao, carros_vendidos, total_vendas)
    print(f"\nO salário final do vendedor é: R$ {salario_final:.2f}")

main()
