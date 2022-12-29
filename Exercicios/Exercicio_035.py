comprimento_reta1 = float(input('Digite o comprimento da primeira reta: '))
comprimento_reta2 = float(input('Digite o comprimento da segunda reta: '))
comprimento_reta3 = float(input('Digite o comprimento da terceira reta: '))
if comprimento_reta1 < comprimento_reta2 + comprimento_reta3 and comprimento_reta2 < comprimento_reta1 + comprimento_reta3 and comprimento_reta3 < comprimento_reta1 + comprimento_reta2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
