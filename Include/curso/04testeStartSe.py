'''

fatorial = int(input('Digite um número: '))
contador = 1

for interador in range(0, fatorial):
    interador = interador + 1
    contador = contador * interador

print(f'fatorial de {fatorial}! = {contador}')
'''


numero = int(input('Digite um número: '))

contador = 1
fatorial = numero

while contador < numero:
    fatorial = fatorial * contador
    contador = contador + 1
print(fatorial)
