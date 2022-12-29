import random

velocidade = random.randint(60, 100)
if velocidade > 80:
    print('Você foi multado!')
    print('Você estava a {} km/h'.format(velocidade))
    print('Você deve pagar R$ {:.2f}'.format((velocidade - 80) * 7))
else:
    print('Você não foi multado!')
