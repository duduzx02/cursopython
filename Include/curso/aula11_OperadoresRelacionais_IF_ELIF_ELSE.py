'''

Operadores Relacionais
    ==, igual
    >, maior que
    >=, maior ou igual
    <, menor que
    <=, menor ou igual
    != difernte

'''

um = 1
dois = 2

igual = um == dois
maior = um > dois
maiorigual = um >= dois
menor = um < dois
menorigual = um <= dois
difernete = um != dois

print(f'{um} == {dois}: {igual}')
print(f'{um} > {dois}: {maior}')
print(f'{um} >= {dois}: {maiorigual}')
print(f'{um} < {dois}: {menor} ')
print(f'{um} <= {dois}: {menorigual}'),
print(f'{um} != {dois}: {difernete}')



nome = input('Digite o seu nome: ')
idade = int(input('Digite seu idade: '))
if idade < 20:
    print('Você não tem idade suficiente!')
elif idade >= 20 and idade <= 30:
    print('Você pode fazer um emprestimo')
else:
    print('Você está muito velho para emprestimo.')