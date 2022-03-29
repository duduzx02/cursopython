secreta = 'Barco'
digitada = []
chances = 3


while True:
    if chances <=0:
        print('Você perdeu!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Por favor, digite apenas uma letra.')
        continue

    digitada.append(letra)

    if letra in secreta:
        print(f'A letra {letra} está na palavra secreta.')
    else:
        print(f'A letra {letra} NÃO ESTÁ na palavra secreta.')
        digitada.pop()

    palavra = ''
    for letra_secreta in secreta:
        if letra_secreta in digitada:
            palavra = palavra + letra_secreta
        else:
            palavra = palavra + '_'
    print(palavra)
    if secreta == palavra:
        print(f'A palavra secreta é {secreta}')
        break
    if letra not in secreta:
        chances = chances - 1
    print(f'Você ainda tem {chances} chances')
