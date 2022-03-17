'''

Operadores lógicos

and, As duas comparações tem que ser True
or, Uma ou otra tem que ser True
not, Inverte o sentido da comparação
in e Checar se algo está dentro de alguma coisa
not in Inverte a checagem se algo está dentro de alguma coisa

'''
nome = 'Eduardo Lima'
sobrenome = 'Lima'
nomemeio = 'Souza'
um = 1
dois = 2

e = um != dois and um < dois
ou = um == dois or um < dois
nao = not um == dois
dentro = sobrenome in nome
naodentro = nomemeio not in nome

# Todas afirmações devem ser verdadeiras
print(f'{um} é diferente de {dois} E {um} é menor que {dois}? {e}')
# Uma ou outra deve ser verdadeira para ser TRUE
print(f'{um} é igual a {dois} OU {um} é menor que {dois}? {ou}')
# O not inverte o sentido da comparação
print(f'{um} NÃO é igual a {dois}? {nao}')
# O in checa se algo está dentro de alguma coisa
print(f'O nome {nome} TEM {sobrenome} no nome? {dentro}')
# O not in inverte a checagem se algo está dentro de alguma coisa
print(f'O nome {nome} não tem {nomemeio} no nome? {naodentro}' )
