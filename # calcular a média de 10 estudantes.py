# calcular a média de 10 estudantes
# duas notas por estudante
media_total = 0
contador = 0
for aluno in range (0, 2):
    nota1 = float(input('digite a nota 1: '))
    nota2 = float(input('digite a nota 2: '))
    media = (nota1 + nota2)/2
    media_total = media_total + media
    # media_total += media
    contador = contador + 1


print(f'a média dos alunos é: {media_total/len(range(0, 2))}' )