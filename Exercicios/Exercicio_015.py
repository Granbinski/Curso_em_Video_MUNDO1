km_percorrido = float(input('Digite a quantidade de km percorridos: '))
dias_aluguel = int(input('Digite a quantidade de dias alugados: '))
preco = (km_percorrido * 0.15) + (dias_aluguel * 60)
print('O valor a ser pago é de R${:.2f}'.format(preco))
