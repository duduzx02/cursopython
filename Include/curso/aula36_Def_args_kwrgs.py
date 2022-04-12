'''

Def - Args - Kwargs

'''

'''
def func(* valores):
    print(valores)


lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)
'''


'''
def func(*args):    # aqui é uma tupla
    args = list(args)   #transformando uma tupla em lista
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    args[0] = 20
    print(args)


# lista = [1, 2, 3, 4, 5]
# print(*lista, sep=', ')

func(1, 2, 3, 4, 5, 6)

'''
'''
def func(*args):
    args = list(args)
    for v in args:
        print(v)


func(8, 6, 4, 9, 7)
'''


def func(**kwargs):


    nome = kwargs.get('nome')
    print(nome)
    sobrenome = kwargs.get('sobrenome')
    print(sobrenome)



func(nome='Eduardo', sobrenome='Lima')
