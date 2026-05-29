comprimento = 7.5
largura = 4.5
altura = 4

import math
comprimento = float(input("digite o comprimento (m)"))
largura = float(input("digite a largura (m)"))
altura = float(input("digite a altura (m)"))

area_paredes = 2 * altura * (comprimento+largura)

area_por_caixa = 1.5

caixas = math.ceil(area_paredes/area_por_caixa)

print(f"área total das paredes: {area_paredes:.2f}m²")
print(f"quantidade de caixas necessárias: {caixas}")