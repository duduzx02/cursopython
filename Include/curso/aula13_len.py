usuario = input('Digite seu nome: ')
caracteres = len(usuario)

if caracteres < 6:
    print('Você precisa digitar no mínimo 6 caracteres.')
else:
    print('Você foi cadastrado!')


