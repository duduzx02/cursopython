'''
def mostralinha():
    print('-'*30)


mostralinha()
print('Sistema de alunos')
mostralinha()
mostralinha()
print('Cadastro de funcionários')
mostralinha()
print('Erro do sistema')
mostralinha()

'''


'''
def mensagem(msg):
    print('-'*35)
    print(msg)
    print('-'*35)

mensagem('Sistema de alunos')
mensagem('Cadastro de funcionários')
mensagem('Erro do Sistema')
'''


'''
def soma(n1, n2):
    s = n1 + n2
    print(s)

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
soma(valor1, valor2)

'''


'''

def contador(* num):
    tam = len(num)

    for valor in num:
        print(valor, end=' ')
    print(f'O tamanho do contador é {tam}')



contador(3, 5, 6, 4)
contador(6, 5, 3)

'''



'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos = pos +1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

'''

def soma (* valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Soma os valores {valores} temos {s}')

valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))

soma(valor1, valor2)