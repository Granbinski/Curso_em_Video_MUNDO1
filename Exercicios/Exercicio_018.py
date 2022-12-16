import math

angulo = int(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangent = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangent))
