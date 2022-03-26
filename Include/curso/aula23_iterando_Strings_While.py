#       Índices
#       0123456789.......................33

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

contador = 0
nova = ''

while contador < tamanho_frase:
    nova += frase[contador]
    contador += 1
    print(nova)
print(nova)


