#
#
# def qualquer():
#     return 'Qualquer coisa!'
# def mostra(funcao):
#     return funcao()
#
# executavel = mostra(qualquer)
#
# print(executavel)


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executavel = mestre(fala, 'Eduardo')

print(executavel)