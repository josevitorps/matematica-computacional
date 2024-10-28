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

def obter_criterio():
    while True:
        criterio = input("Digite qual critério você deseja verificar (LAL, AA, LLL) ou '!s' para sair: ").strip().upper()
        if criterio in {"LAL", "AA", "LLL"}:
            return criterio
        elif criterio == "!S":
            print("Funcionamento do programa foi interrompido, obrigado por usar.")
            exit()
        else:
            print("Critério inválido! Por favor, digite LAL, AA, LLL ou '!s' para sair.")

def criterio_lal(lado1_tri1, lado2_tri1, lado1_tri2, lado2_tri2, angulo_tri1, angulo_tri2):
    return (lado1_tri1 / lado1_tri2 == lado2_tri1 / lado2_tri2) and (angulo_tri1 == angulo_tri2)

def criterio_aa(angulo1_tri1, angulo2_tri1, angulo1_tri2, angulo2_tri2):
    return (angulo1_tri1 == angulo1_tri2) and (angulo2_tri1 == angulo2_tri2)

def criterio_lll(lado1_tri1, lado2_tri1, lado3_tri1, lado1_tri2, lado2_tri2, lado3_tri2):
    return (lado1_tri1 / lado1_tri2 == lado2_tri1 / lado2_tri2 == lado3_tri1 / lado3_tri2)

def verificar_semelhanca(triangulo1, triangulo2, criterio):
    if criterio == "LAL":
        if criterio_lal(triangulo1[0], triangulo1[1], triangulo2[0], triangulo2[1], triangulo1[3], triangulo2[3]):
            return "Os triângulos são semelhantes pelo critério LAL."
    elif criterio == "AA":
        if criterio_aa(triangulo1[3], triangulo1[4], triangulo2[3], triangulo2[4]):
            return "Os triângulos são semelhantes pelo critério AA."
    elif criterio == "LLL":
        if criterio_lll(triangulo1[0], triangulo1[1], triangulo1[2], triangulo2[0], triangulo2[1], triangulo2[2]):
            return "Os triângulos são semelhantes pelo critério LLL."
    return "Os triângulos não são semelhantes."

criterio = obter_criterio()

print("\nDigite os lados e ângulos do primeiro triângulo (ou '!s' para sair):")
lado1_tri1 = obter_valor_float("Lado 1: ")
lado2_tri1 = obter_valor_float("Lado 2: ")
lado3_tri1 = obter_valor_float("Lado 3: ")
angulo1_tri1 = obter_valor_float("Ângulo 1: ")
angulo2_tri1 = obter_valor_float("Ângulo 2: ")

print("\nDigite os lados e ângulos do segundo triângulo (ou '!s' para sair):")
lado1_tri2 = obter_valor_float("Lado 1: ")
lado2_tri2 = obter_valor_float("Lado 2: ")
lado3_tri2 = obter_valor_float("Lado 3: ")
angulo1_tri2 = obter_valor_float("Ângulo 1: ")
angulo2_tri2 = obter_valor_float("Ângulo 2: ")

triangulo1 = [lado1_tri1, lado2_tri1, lado3_tri1, angulo1_tri1, angulo2_tri1]
triangulo2 = [lado1_tri2, lado2_tri2, lado3_tri2, angulo1_tri2, angulo2_tri2]

resultado = verificar_semelhanca(triangulo1, triangulo2, criterio)
print("\nResultado:", resultado)
