'''

Operador ternário

'''

'''
logged_user = True
if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário off'

print(msg)

'''



'''
logged_user = False
msg = 'ON' if logged_user else 'OFF'
print(msg)

'''



idade = int(input('Qual sua idade: '))
maior = idade >= 18
msg = 'Maior' if maior else 'Menor'
print(msg)