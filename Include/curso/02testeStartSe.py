x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if x > y:
    print(x)
elif y > x:
    print(y)
else:
    print(f'Números digitados iguais! {x} e {y}')
