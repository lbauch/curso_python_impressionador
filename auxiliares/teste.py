# Arquivo destinado para realização de pequenos testes de funcionamento

def minha_soma(arg1, arg2, *args1, arg3, arg4, **args2):
    soma = 0
    soma += arg1 - arg2
    print(soma)
    for arg in args1:
        soma += arg
    print(soma)
    soma += arg3 + arg4
    print(soma)
    for args in args2:
        print(args)

# Atribui quantos parâmetros forem necessários.
print(minha_soma(10, 5, 1, 10, arg1 = 90, arg2 =  0, arg3 = 9, arg4 = 8))