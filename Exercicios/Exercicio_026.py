palavra = str(input('Digite uma palavra: '))
letra_a = palavra.count('a')
posicao_a = palavra.find('a')
ultima = palavra.rfind('a')
print('A letra "a" aparece {} vezes na palavra.'.format(letra_a))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(posicao_a))
print('A letra "a" aparece pela última vez na posição {}.'.format(ultima))