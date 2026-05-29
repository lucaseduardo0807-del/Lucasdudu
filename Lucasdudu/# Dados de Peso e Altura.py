# Dados de Peso e Altura
def calcularImc(peso,altura):
    imc = peso / (altura*altura)
    return imc

def classificacao(IMC):
    if IMC < 16.9:
        return('Muito abaixo do peso')
    elif 17<= IMC <=18.4:
        return('Abaixo do peso')
    elif 18.5<= IMC <=24.9:
        return('Peso normal')
    elif 25<= IMC <=29.9:
        return('Acima do peso')
    elif 30 <= 34.9:
        return('Obesidade grau 1')
    elif 35 <= 40:
        return('Obesidade grau 2')
    else:
        return('Obesidade grau 3')
    
print("Programa Principal")
n = int(input("digite o numero de testes: "))
for i in range(1, n + 1):
    print(f"pessoa: {i}")
    peso = float(input("digite seu peso: ").replace("," , "."))
    altura = float(input("digite sua altura: ").replace("," , "."))
    imc = calcularImc(peso,altura)
    classifica = classificacao(imc)
    print(f"IMC: {imc:.2f} ")
    print(f"classificação: {classifica}")

print("Fim do programa")