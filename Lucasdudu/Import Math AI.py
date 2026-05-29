import math #"AI"

print("--- Calculador de Azulejos para Cozinha ---")

# 1. Entrada de dados
comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
largura = float(input("Digite a largura da cozinha (em metros): "))
altura = float(input("Digite a altura da cozinha (em metros): "))

# Cada caixa cobre 1.5 metros quadrados
METRAGEM_POR_CAIXA = 1.5

# 2. Processamento dos dados
# Calcula a área das paredes duas a duas
area_paredes_comprimento = 2 * (comprimento * altura)
area_paredes_largura = 2 * (largura * altura)

# Área total a ser azulejada
area_total = area_paredes_comprimento + area_paredes_largura

# Quantidade de caixas necessárias (arredondada para cima, pois não vendem fração de caixa)
caixas_necessarias = math.ceil(area_total / METRAGEM_POR_CAIXA)

# 3. Exibição dos resultados
print("\n--- Resultado do Cálculo ---")
print(f"Área total das paredes: {area_total:.2f} m²")
print(f"Quantidade de caixas de azulejo necessárias: {caixas_necessarias} caixas")