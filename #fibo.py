#fibo
#parar no número 2000 da sequência
0 1 1 2 3 5

anterior = 0
atual = 1
proximo = anterior + atual # 1 = 1 + 0

while proximo < 2000:
anterior = atual # 1
atual = proximo # 1
proximo = anterior + atual # 2 = 1 + 1

anterior = atual # 2
atual = proximo # 3
proximo = anterior + atual # 5 = 1 + 2