numero = input('Digite um número: ')

if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
else:
    print('O que você digitou não é inteiro.')
