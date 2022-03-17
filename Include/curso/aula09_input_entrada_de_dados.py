'''

Entrada de dados

'''

nome = input('Qual é o seu nome? ')
print(f'O usuário digitou {nome} e tipo da variável é'
      f'{type(nome)}')
# Toda entrada de dados na função input será uma String

print()
print()

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} e nasceu em {nascimento}.')

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

print(numero1 + numero2)

# * A função input sempre retorna uma string, independente do que for digitado pelo usuário.

# Em programação, os termos "fazer cast" ou "type cast" referem-se à conversão de um tipo de valor em outro tipo de valor. Sabendo disso, qual o tipo da variável "outra_variavel" abaixo?

# variavel = '5.5'
# outra_variavel = (int(float(variavel)))

# Resposta
#       Primeiro a "variavel" era uma string, depois convertida em float e, por fim, em int. Posteriormente, salvamos o valor da "variavel" em "outra_variavel". Portanto, o valor final é do tipo int.

