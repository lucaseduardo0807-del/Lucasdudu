# Jogo de Pedra, Papel ou Tesoura
import random

def jogar():
    itens = ['pedra', 'papel', 'tesoura']

    jogador = input("Escolha pedra, papel ou tesoura: ").lower().strip()

    if jogador not in itens:
        print("ERROR 404")
        return

    computador = random.choice(itens)
    
    print(f"\nVocê escolheu: {jogador.capitalize()}")
    print(f"O computador escolheu: {computador.capitalize()}")
    
    if jogador == computador:
        print("Empate")
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print("YOU WIN!!!")
    else:
        print("YOU LOSE !!!")

if __name__ == "__main__":
    jogar()