'''

for in
Iterando strings com for
função range(start=0, stop, step=1)

continue - pula para o proximo laço
break - termina o laço

'''


texto = 'python'

for n, letra in enumerate(texto):
    print((n, letra), end='')


print()
print('-'*35)
print()


for i in range(10, 0, -1):
    print(i)

print()
print('-'*35)
print()

for i in range(10):
    print(i)

print()
print('-'*35)
print()

texto1 = 'curso python'
novote = ''
print(texto1)
for letra in texto1:
    if letra == 'c':
        novote = novote + letra.upper()
    elif letra == 'p':
        novote += letra.upper()
    elif letra == 'n':
        novote += letra.upper()
    else:
        novote = novote + letra
print(novote)
