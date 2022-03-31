'''

for  /  else

'''

variavel = ['Eduardo', 'Augusto', 'lívia', 'Arthur']

for valor in variavel:
    if valor.lower().startswith('a'):   # .startswith() Chega a primeira palavra, e .lower() transforma o valor em lower
        print('Começa com A', valor)
    else:
         print('Essa não começam com A,', valor)

