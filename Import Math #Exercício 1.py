import math #Principal
potencia_lampada = 5
largura = 3
comprimento = 5

# area -> descobrir metragem
area = largura * comprimento
# descobrir quantos watts eu preciso
potencia_necessaria = area * 3
# descobrir numero de bocais
num_bocais = math.ceil(area/3)
# calcular a quantidade de lampadas
quantidade_lampadas = potencia_necessaria
print(f'Potencia Necessaria: {potencia_necessaria}')
print(f"quantidade de lampadas: {quantidade_lampadas}")
print(f'Numero bocais: {num_bocais}')
if quantidade_lampadas > num_bocais:
    print('Precisamos de lampadas mais fortes')
else:
    print('Tudo iluminado')