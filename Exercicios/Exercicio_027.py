nome_completo = input('Digite o nome completo: ')
separa_nome = nome_completo.split()
primeiro_nome = separa_nome[0]
ultimo_nome = separa_nome[len(separa_nome) - 1]
print('O primeiro nome é {}.'.format(primeiro_nome))
print('O último nome é {}.'.format(ultimo_nome))
