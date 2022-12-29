distancia_km = float(input('Qual a distância da sua viagem? '))
if distancia_km <= 200:
    print('Você pagará R$ {:.2f}'.format(distancia_km * 0.50))
elif distancia_km > 200:
    print('Você pagará R$ {:.2f}'.format(distancia_km * 0.45))
else:
    print('Erro!')
