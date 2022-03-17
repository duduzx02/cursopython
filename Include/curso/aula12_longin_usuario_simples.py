login = input('Nome do usuário: ')
senha = input('Senha: ')

login_bd = 'Eduardo'
senha_bd = '123456'

if login == login_bd and senha == senha_bd:
    print('Logado!')
else:
    print('Login ou senha inválida!')
