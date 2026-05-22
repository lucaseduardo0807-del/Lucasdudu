# receba 3 numeros do usuario
# imprima o maior deles

num1 = float (input('Escolha um número:\n'))
num2 = float (input('Escolha um número:\n'))
num3 = float (input('Escolha um número:\n'))
maior = num3 # null -> Vazio -> Python = None
if num1 > num2: and num1> num3:
    maior = num1
elif num2 > num3:
    maior = num2

print (f'O maior número é: {maior}')