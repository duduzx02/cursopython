def area(largura, comprimento):
    ar = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {ar} m²')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)