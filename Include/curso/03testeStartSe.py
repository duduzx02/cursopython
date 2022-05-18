nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

media = ((nota1 * 2) + (nota2 * 2) + nota3) / 5

if media >= 6.0:
    print(f'APROVADO! Sua média {media}')
elif media >= 3.0:
    print(f'RECUPERAÇÃO! Sua média {media}')
else:
    print(f'REPROVADO Sua média {media}')
