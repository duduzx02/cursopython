'''
a = lambda x, y: x * y

print(a(2, 8))
'''

lista = [
    ['p1', 13],
        ['p2', 14],
        ['p3', 8],
        ['p4', 5],
        ['p5', 52],
        ['p6', 47],
]


# lista.sort(key=lambda item: item[1], reverse=True)
# print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))