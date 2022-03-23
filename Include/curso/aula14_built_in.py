num = input('Digite um número: ')
num2 = input('Digite outro número: ')

# isnumeric
# isdigit
# isdecimal
# Números e positivos (12345648598)

print(num.isnumeric())
print(num.isdigit())
print(num.isdecimal())

print()
print(num2.isnumeric())
print(num2.isdigit())
print(num2.isdecimal())


try:
    num = int(num)
    num2 = int(num2)

    print(num + num2)
except:
    print('Nem todos os caracteres são apenas inteiros.')