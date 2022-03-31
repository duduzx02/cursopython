'''

Split, Join, Enumerate
* Split - dividi uma string
* Join - junta uma lista
* Enumerate - enumera elementos da lista

'''



'''

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = string.split(' ')   # Onde tiver espaço vai ser trocado por um indice


for valor in lista:
    print(f'A palavra {valor}, apareceu {lista.count(valor)}x na frase')

'''



'''

palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra {palavra}, apareceu {contagem}x')

'''



'''
string = 'O Brasil é penta'
lista = string.split(' ')
string2 = '/'.join(lista)
print(string)
print(lista)
print(string2)

'''


'''
string = 'O Brasil é penta.'
lista = string.split(' ')

print(string)
for indice, palavra in enumerate(lista):
    print(f'O índice da palavra {palavra} é {indice}')
    print(f'O índice da palavra {lista[indice]} é {indice}')
    
'''



'''

lista = [
    [0, 'B'],
    [1, 'D'],
    [2, 'F']
]

for numero in (lista):
    print(numero[0], numero[1])

'''



lista = ['Du', 'Dudu', 'Edu']

for indice, nome in enumerate(lista):
    print(indice, nome)