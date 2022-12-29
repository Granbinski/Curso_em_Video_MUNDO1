numero = int(input('Digite um número: '))
caulculo = numero % 2
if caulculo == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))
