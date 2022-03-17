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
