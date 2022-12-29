ano_inicio = int(input('Digite o ano de inicio: '))
ano_fim = int(input('Digite o ano de fim: '))

cont = 0

for ano in range(ano_inicio, ano_fim + 1):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano)
        cont += 1
print('Existem {} anos bissextos'.format(cont))
