cpf = input('digite seu cpf: ')
total = 0
for indice, contador in enumerate(range(10, 1, -1)):
    num = int(cpf[indice])
    total = total + (num * contador)
    print(num, contador)
print(total)
if total == 297:
    total = 0
    cpf = input('Digite novamente seu cpf: ')
    for indice, contador in enumerate(range(11, 1, -1)):
        num = int(cpf[indice])
        total = total + (num * contador)
        print(num, contador)
print(total)


