import random

nome_alunos = ['João', 'Maria', 'José', 'Ana']
ordem_apresentacao = random.sample(nome_alunos, len(nome_alunos))
print('A ordem de apresentação será: {}'.format(ordem_apresentacao))
