nome_completo = str(input('Digite seu nome completo: ')).strip()
print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo) - nome_completo.count(' '))
print('O primeiro nome tem {} letras.'.format(nome_completo.find(' ')))