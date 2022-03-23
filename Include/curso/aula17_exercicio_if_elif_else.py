hora = input('Que horas são? (0-23): ')

if hora.isnumeric():
    hora = int(hora)
    if hora <= 11:
        print('Bom dia!')
    elif hora <= 17:
        print('Boa tarde! ')
    elif hora <=23:
        print('Boa noite!')
    else:
        print('Por favor, digite um hoário entre 0 e 23! ')
else:
    print('O que você digitou não é inteiro.')