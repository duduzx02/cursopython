nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4 and tamanho != 0:
    print('Seu nome é curto! ')
elif  tamanho <=6:
    print('Seu nome é normal! ')
elif tamanho > 6:
    print('Seu nome é muito grande! ')
else:
    print('Você não digitou nada!')
