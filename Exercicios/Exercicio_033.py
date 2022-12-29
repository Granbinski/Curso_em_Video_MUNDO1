primeiro_num = int(input('Digite o primeiro número: '))
segundo_num = int(input('Digite o segundo número: '))
terceio_num = int(input('Digite o terceiro número: '))
if primeiro_num > segundo_num and primeiro_num > terceio_num:
    print('O primeiro número é o maior')
elif segundo_num > primeiro_num and segundo_num > terceio_num:
    print('O segundo número é o maior')
elif terceio_num > primeiro_num and terceio_num > segundo_num:
    print('O terceiro número é o maior')
else:
    print('Os três números são iguais')


if primeiro_num < segundo_num and primeiro_num > terceio_num:
    print('O primeiro número é o maior')
elif segundo_num < primeiro_num and segundo_num > terceio_num:
    print('O segundo número é o maior')
elif terceio_num < primeiro_num and terceio_num > segundo_num:
    print('O terceiro número é o maior')
else:
    print('Os três números são iguais')
