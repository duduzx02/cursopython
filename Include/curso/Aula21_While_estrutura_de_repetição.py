'''

While
Utilização para realizar ações enquanto uma condição
for verdadeira.

'''

c = 0
while c < 10:
    if c == 3:
        c = c +1
        continue
    print(c)  # Aqui mostra apartir do 0, mas tira o 100
    c = c + 1
    #  print(c) # Aqui mostra apartir de 1, mas tira o 0
print('Acabou')

print('-'*25)

z = 0
while z < 5:
    if z == 3:
        z = z + 1
        break
    z = z + 1
    print(z)

print('-'*25)

x = 0
while x < 5:
    y = 0
    while y < 2:
        print(f'({x}),({y})')
        y = y + 1
    x = x + 1
