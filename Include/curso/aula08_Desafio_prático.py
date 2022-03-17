nome = 'Eduardo'
idade = 26
peso = 96
altura = 1.76
ano_atual = 2022
dataNascimento = ano_atual - idade
imc = peso / (altura ** 2)
print(f'{nome} tem {idade} anos, {altura:} e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {dataNascimento}.')

'''

* Utilizamos o caractere # (cerquilha) antes de um comentário em Python.

* Print é uma função usada para exibir coisas na tela. Chamamos este processo de "imprimir" na tela. O comando anterior imprime "Já sei!" no output do Python.

* Apesar de importantes, não devemos comentar todas as linhas do nosso código. O código bem escrito deve ser de fácil entendimento. Se você precisa comentar todas as linhas do seu código, este código não foi bem escrito.

* string é uma cadeia de caracteres (texto dentro de aspas), int são valores inteiros (10, 11, -11), bool são valores booleanos (True ou False) e float são números de ponto flutuante (10.5, 1.80...)

* Não é possível usar o operador de + (mais) com uma string e um inteiro.

* O sinal de % não faz porcentagem, mas retorna o resto da divisão entre dois números. Dois asteriscos fazem potenciação.

* Em uma linguagem de tipagem dinâmica e forte, o próprio interpretador determina o tipo de um valor quando criado. É possível modificar um valor interpretado de um tipo para outro realizando um "Type Cast" (ou cast) em alguns casos, mas o interpretador não fará isso por você.
'''