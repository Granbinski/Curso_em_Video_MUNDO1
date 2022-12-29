import random
numero_aleatori = random.randint(0, 5)
numero_jogador = int(input('Digite um número de 0 a 5: '))
if numero_aleatori == numero_jogador:
    print('Você acertou!')
else:
    print('Você errou!')
