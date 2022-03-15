'''
+ - Adição
- - Subtração
* - Multiplicação
/ - Divisão
// - divisão inteira
** - potenciação
% - O resto da divisão
() - muda a ordem da precedencia

# Ordem de precedência
1º ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

2º ** - Depois vem a exponenciação

3º * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

4º +  - - Por fim, soma e subtração

'''


print('Adição', 3 * 2)
print('Subtração', 3 - 2)
print('Multiplicação', 3*2)
print('Divisão', 3/2)
print('Divisão inteira', 3//2)
print('Potenciação', 3**2)
print('O resto da divisão', 3%2)
print(' 5+2*10 Sem parênteses ', 5+2*10)
print('(5+2)*10 Com parênteses', (5+2)*10)

