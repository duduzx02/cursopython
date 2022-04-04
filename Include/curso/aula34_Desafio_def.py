#
#
# def saudacao(saudacao, nome):
#     print(saudacao, nome)
#
# saudacao('Oi', 'Eduardo')
#
#





# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)
#
# soma(1, 2, 3)
# soma(10, 10, 10)







# def numeros(n1, n2):
#     return n1, ((n1 * n2) / 100) + n1
#
# print(numeros(10, 10))
# print(numeros(100, 10))




def fizzbuzz(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return f'FizzBuzz, {n1} é divisível por 3 e 5'
    if n1 % 5 == 0:
        return f'Buzz, {n1} é divisível por 5'
    if n1 % 3 == 0:
        return f'Fizz, {n1} é divisível por 3'
    return n1

from random import randint

for i in range (100):
    aleatorio = randint(0, 100)
    print(fizzbuzz(aleatorio))



