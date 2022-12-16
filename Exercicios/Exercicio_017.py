comprimento_oposto = float(input('Digite o comprimento do cateto oposto: '))
comprimento_adjacente = float(
    input('Digite o comprimento do cateto adjacente: '))
comprimento_hipotenusa = (comprimento_oposto ** 2 +
                          comprimento_adjacente ** 2) ** (1 / 2)
print('O comprimento da hipotenusa é {:.2f}'.format(comprimento_hipotenusa))
