frase = 'o rato roeu a roupa do rei de roma'  # valor  interavel
tamanho = len(frase)
contador = 0
novaFrase = ''

letra1 = input('Qual letra você quer ?')

while contador < tamanho:
    letra = frase[contador]
    if letra == letra1:
        novaFrase += letra1.upper()
    else:
        novaFrase += letra
    contador += 1
print(novaFrase)