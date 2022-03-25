while True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    operador = input('Digite um operador: ')


    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Você digitou o operador errado.')