#Laço for
for i in range(0,4,1):
    print(1)

# Imprimindo com variáveis
var1 = 10
print(f"Faturamento Pepsi: {var1:,.2f}")
print(f'em centímetros: {var1 / 100}')
print('em centímetros: {var1 / 100}')

# in; str
# Upper
alcoolico = 'bac'
print('Código é de bebida alcóolica? ' + str('BAC' in alcoolico.upper()))
print('Lucas' in 'Meu nome é Lucas')
print('lucas' in 'Meu nome é Lucas')

# if elif else
if var1 < 5:
    print(f'{i} é menor que 5')
elif var1 == 5:
    print(f'{i} é igual a 5')
else:
    print(f'{i} é maior que 5')

# Repetição para ler int
# Laço while
# Try Except
while True:
    try:
        total_estoque = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Comparação de Strings
# Len
s1 = input('String 1: ')
s2 = input('String 2: ')
if len(s1) == len(s2):
    print('As strings são de tamanhos iguais.')  
if s1 == s2:
    print('As strings possuem conteúdos iguais.')

# Split - divide um texto em array de strings
s1 = "texto de exemplo qualquer\nparte 2 exemplo"
# Por padrão, o split separa espaços, \n e \t
s_novo = s1.split()
print(s_novo)
# É possível separar somente por quebra de linhas
s_novo = s1.split('\n')
print(s_novo)
# É possível definir algum valor para separar os textos
s_novo = s1.split('o')
print(s_novo)

#conversão len para String - sem a conversão, resulta em erro.
email = 'lucasb@gmail'
print('Tamanho do email:' + str(len(email)))

# Extrair partes de string
tel = input('Telefone: ')
print(f'Telefone corrigido com formatação: {tel[:4]}-{tel[4:]}')

# Replace
tel = tel.replace('-', '')

# Format
custo = 500
faturamento = 270
lucro = faturamento - custo
print('o faturamento: {}, custo: {}, lucro: {}'.format(faturamento, custo, lucro))
print('Faturamento foi {:+,} e lucro foi {:+,}'.format(faturamento, lucro))
print('Faturamento foi {:.2f} e lucro foi {:2f}'.format(faturamento, lucro))
lucro_texto = 'R${:_.2f}'.format(faturamento - custo)


# Concatenação de Strings
print('1' + '2')
print(1 + 2)

# Listas
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
# Iterador
i = produtos.index('geladeira')
produto_escolhido = produtos[i]

# Substituir item
produtos[2] = 'Iphone 11'
# Adicionar item ao final
produtos.append('Iphone 12')
# Remover pelo nome - Não pode ser armazenado em variável
# Recomendado sempre botar em try except, pois, caso não possua, resulta em erro.
produto = input('Digite o produto:\n')
try:
    # produtos.remove('celular')    
    produtos.remove(produto)
except:
    print(f'produto {produto} não existe')
# Remove pelo índice - pode ser armazenado em variável
produto_removido = produtos.pop(5)

# Max, min, index
vendas = [  1000,    1500  ,   350  ,    270   ,    900  ]
tamanho = len(produtos)
mais_vendido = max(vendas)
menos_vendido = min(vendas)

i = vendas.index(mais_vendido)
prod_mais_vendido = produtos[i]

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
novos_produtos = ['Iphone 12', 'Iphone 13']

# Concatena as listas, criando uma nova variável
todos_produtos = produtos + novos_produtos

# Append - altera a lista 1, inserindo a 2
# produtos.append(novos_produtos)
# print(produtos)
# Saída: ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno', ['Iphone 12', 'Iphone 13']]
# Não sai adequadamente
# O correto é utilizar extend
produtos.extend(novos_produtos)
# Saída: ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno', 'Iphone 12', 'Iphone 13']
print(produtos)

# concatenando vetores ou somando variáveis
print([1] + [2])
print(1 + 2)

# Organizar listas
# Organização decresente
vendas.sort(reverse=True)
# Organização cresente
vendas.sort()

# Juntando valores de lista em uma string
print('\n'.join(produtos))
lista = ', '.join(produtos)
# Separando novamente a lista
print(produtos)
produtos = lista.split
print(lista)
# Para mais métodos, consultar https://docs.python.org/3/tutorial/datastructures.html

# Alterações incrementais
var1 = 10
var1 = var1 + 5
print(var1)
var1 += 6
print(var1)