'''

Funções (def) e (return)

'''

'''

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

resultado = divisao(8, 2)

if resultado:
    print(resultado)
else:
    print('Conta inválida.')
 
'''



def dumb():
    return 10  # Se coloca qualquer dado aqui

print(dumb(), type(dumb()))

