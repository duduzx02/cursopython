variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor'
    print(variavel)

def func3():
    global variavel
    variavel = 'outro valor'

def func4(arg=None):
    arg = arg.replace('v', 'c')
    return arg


outro = func4(arg=variavel)
print(outro)

func()
func2()
func3()

print(variavel)


