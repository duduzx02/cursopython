'''

Manipulando Strings
* String indices
* Fatiamento de Strings [incio:fim:passo]
* Funções bult-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html

'''
texto = 'python <3'
print(len(texto)) #Resultado 9, mas no python a contagem começa com 0
print(texto[8])
print(texto[-1])

print(texto[-(len(texto))])
print(texto[0])
print(texto[-0])

url = 'www.google.com.br/'
print(url[:-1])


# fatiamento

novotexto = texto[:6]
finaltexto = texto[6:]
textoreverso = texto[::-1]
print(novotexto)
print(finaltexto)
print(textoreverso)
