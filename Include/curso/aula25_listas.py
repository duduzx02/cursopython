'''

Listas
fatiamento
append, insert, pop, del, clear, extend, min, max, range

'''

lista = [1, 2, 'Eduardo', 1.6]
for i, indic in enumerate(lista):
    print(i ,indic)

print()
print('-'*35)
print()

lista2 = ['eduardo', 'Lima']
lista2[1] = 'De Souza Lima'
print(lista2[1])
print(lista2[1][1])

print()
print('-'*35)
print()

l0 = ['l0', 1, 2, 3]
l1 = ['l1', 1, 2, 3]
l2 = ['l2', 4, 5, 6]
l3 = 'l3', l1 + l2
l4 = ['l4', 1, 2, 3, 4, 5, 6, 7, 8, 9]
l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l6 = list(range(1, 10))
l7 = ['String', True, 10, -24.00]


print(l1, l2, l3)

print(l1)
l1.extend(l2)   # Pode colocar qualquer coisa, desde que seja apenas 1
print(l1)

print('-'*35)

print(l2)
l2.append(l3)  # adiciona um valor no final da lista
print(l2)

print('-'*35)

print(l0)
l0.insert(0, 0)     # posso colocar qualquer coisa em qualquer indice
print(l0)

print('-'*35)

l0.pop(2)   # remove o índice 2
print(l0)

print('-'*35)

print(l4)
del(l4[6:9])    # Remove os valores dos índices de 6:9
print(l4)
del(l4[6])      # Remove o valor do índice 6
print(l4)

print('-'*35)

print(l5)
print(max(l5))
print(min(l5))

print('-'*35)

print(l6)

print('-'*35)

for valor in l7:
    print(f'O valor de {valor} é {type(valor)}')

print('-'*35)


