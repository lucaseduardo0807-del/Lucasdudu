#aula7-funções
#Programa Principal (Soma)
def somar (a,b):
    return a + b
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
soma = somar(num1,num2)
print(f'soma: {soma}')

# Divisão
def dividir (a,b):
    return a / b
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
divisão = dividir(num1,num2)
print(f'divisão: {divisão}')

# Multiplicação
def multiplicar (a,b):
    return a * b
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
multiplicação = multiplicar(num1,num2)
print(f'multiplicação: {multiplicação}')

# Subtração
def subtrair (a,b):
    return a - b
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
subtração = subtrair(num1,num2)
print(f'subtração: {subtração}')

# Média
def mediar (a,b):
    return (a+b) / 2
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
média = mediar(num1,num2)
print(f'média: {média}')