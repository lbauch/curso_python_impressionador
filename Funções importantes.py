#Laço for
for i in range(0,4,1):
    print(i)

print('break')

for i in range(0,9,2):
    print(i)

print('break')

for i in range(5,9,2):
    print(i)

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
    # produtos.remove('celular') - remove pelo nome, não armazena em variável.
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
top3 = ['tv', 'celular', 'tablet']
# map
# Utilizando o join com valores inteiros
# Necessário utilizar o map, para mapear como string
string_top3 = ', '.join(map(str, top3))

print(f'Os 3 maiores valores de venda são, respectivamente: {string_top3}')
# Separando novamente a lista
print(produtos)
# split
produtos = lista.split
print(lista)
# Para mais métodos, consultar https://docs.python.org/3/tutorial/datastructures.html

produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]
# Atribuir valores a um array:
for i in range(len(produtos_ecommerce)):
    vendas, preco = produtos_ecommerce[i]
    print(f'vendas:{vendas}; preco:{preco}')

# for in:
for produto_iterador in produtos:
    print(produto_iterador)

# for in, enumerate - percorre a lista e numera o índice.
# torna-se mais lento
funcionarios = ['Maria', 'José', 'Lucas']
for i , funcionario in enumerate(funcionarios):
    print('{} é o funcionário {}'.format(i, funcionario))

# Alterações incrementais
var1 = 10
var1 = var1 + 5
print(var1)
var1 += 6
print(var1)

# As duas variáveis apontam para o mesmo endereço de memória.
lista1 = ['item1', 'item2', 'item3']
lista2 = lista1
lista2.pop()
print(lista1)
lista1 = ['item1', 'item2', 'item3']
# Necessário o comando copy para criar uma nova variável. Os dois pontos indicam que quero copiar todos os valores de até, quando estiver vazio, mínimo e máximo índica.
lista2 = lista1.copy()
print(lista2)
lista2 = lista1[:]
print(lista2)
lista2 = lista1[1:]
print(lista2)
lista2 = lista1[:2]
print(lista2)
lista2 = lista1[1:3]

# Listas de listas - matrizes
vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]
vendas_ipad_joao = vendas[1][0]
print(vendas_ipad_joao)

# Digitando com moedas
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_ano = vendas_1sem + vendas_2sem
vendas_melhor_mes = max(vendas_ano)
vendas_pior_mes = min(vendas_ano)
melhor_mes = meses[vendas_ano.index(vendas_melhor_mes)] 
print(f'O melhor mês do ano foi "{melhor_mes}", com R$ {vendas_melhor_mes:.2f} em vendas'.replace('.',',') + \
        '.\n' + f'O total de vendas do pior mês foi R$ {vendas_pior_mes:.2f}'.replace(".",","))

# Soma total de um array
faturamento = sum(vendas_ano)

#Tornar a peimeira letra maiúscula
string_top3.capitalize()