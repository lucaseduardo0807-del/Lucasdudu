import math #"AI-2"

print("--- Calculador de Iluminação Residencial ---")

# 1. Entrada de dados
potencia_lampada = float(input("Digite a potência da lâmpada que deseja usar (em Watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# 2. Processamento dos dados
area = largura * comprimento
potencia_total_necessaria = area * 3
bocais_disponiveis = math.floor(area / 3)  # Arredonda para baixo, pois bocais precisam de espaço físico completo

# Cálculo de lâmpadas necessárias para atingir a potência
# math.ceil é usado para arredondar para cima (ex: se der 2.1 lâmpadas, você precisará de 3)
lampadas_necessarias = math.ceil(potencia_total_necessaria / potencia_lampada)

# 3. Exibição dos resultados
print("\n--- Resultado da Análise ---")
print(f"Área do cômodo: {area:.2f} m²")
print(f"Potência total necessária para o ambiente: {potencia_total_necessaria:.2f} W")
print(f"Quantidade de bocais disponíveis no teto: {bocais_disponiveis}")
print(f"Quantidade de lâmpadas de {potencia_lampada}W necessárias: {lampadas_necessarias}")

# Validação extra: e se o número de lâmpadas for maior que os bocais?
if lampadas_necessarias > bocais_disponiveis:
    print("\n[Aviso] Atenção: A quantidade de lâmpadas necessárias excede o número de bocais disponíveis!")
    print("Sugestão: Utilize lâmpadas de maior potência para reduzir a quantidade necessária.")