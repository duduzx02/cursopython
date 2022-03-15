"""
Tipos de dados
str - string - textos 'aspas simples' "Duplas"
int - inteiro - 1  6  -30  -80 e 0
float - real/ponto flutuante -  10.50  1.5  -10.50 0.0
bool - booleano/lógico - True/False
"""

# Type é uma classe e ela retorna o tipo do argumento

print('Eduardo', type('Eduardo'))
print(10, type(10))
print(0.0, type(0.0))
print(10 == 10, type(10 == 10))
print('l' == 'L', type('l' == 'L'))

# Convertendo um tipo para outro tipo

print('Dudu', type('Dudu'), type(bool('Dudu')), type('Dudu'))
print('10', type('10'), type(int('10')))



