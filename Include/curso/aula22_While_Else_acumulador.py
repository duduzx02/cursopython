'''

while / else
contadores e acumuladores

'''

contador = 1
acumulador = 1

while contador <= 10:
    print(acumulador, contador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
print('Isso será executado.')


print()
print('-'*30)
print()

c = 1
ac = 1

while c < 10:
    print(c, ac)
    c = c + 1
    ac = ac + c
    if c == 5:
        break
else:
    print('Cheguei no else.')
print('Isso será executado.')