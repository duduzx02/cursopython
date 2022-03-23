'''

Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de pnt flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float) Ex: :.2f
:(Caractere)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

'''


x = 1
y = 3
divisao = x / y
print(f'{divisao:.2f}')

print(f'{x:0^9}')

nome = 'Eduardo Lima'
print(nome.upper())
print(nome.lower())
print(nome.capitalize())