altura_parede = float(input('Qual a altura da parede? '))
largura_parede = float(input('Qual a largura da parede? '))
metros_quadrados = altura_parede * largura_parede
tinta = metros_quadrados / 2
print('A area da parede é {} m²'.format(metros_quadrados))
print('Você vai precisar de {} l de tinta'.format(tinta))
