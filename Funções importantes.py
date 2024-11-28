
#------Laço for
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

# in
alcoolico = 'bac'
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
# ------Laço while
# Try Except
# WHILE
while True:
    try:
        total_estoque = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")


# ------Strings

# str - transformar em string
# Upper -maiúsculas
print('Código é de bebida alcóolica? ' + str('BAC' in alcoolico.upper()))

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

#Tornar a primeira letra maiúscula
email.capitalize()

# Format
custo = 5000
faturamento = 2700
lucro = faturamento - custo
print('o faturamento: {}, custo: {}, lucro: {}'.format(faturamento, custo, lucro))
# Neste caso, insere sempre o sinal na frente, mesmo que seja positivo, e insere a vírgula como separador de milhar.
print('Faturamento foi {:+,} e lucro foi {:+,}'.format(faturamento, lucro))
# .2, .1 indica a qtd de casas decimais
print('Faturamento foi {:.2f} e lucro foi {:2f}'.format(faturamento, lucro))
# Porcentagem
print('Faturamento foi {:.1%}'.format(faturamento))
# o underline(_)cria separador de milhares com _
lucro_texto = 'R${:_.2f}'.format(faturamento - custo)
print(lucro_texto)
lucro_texto = 'R${:_.2f}'.format(faturamento - custo).replace('.',',').replace('_','.')
print(lucro_texto)


# Concatenação de Strings
print('1' + '2')
print(1 + 2)

# ------Listas
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
# Iterador
i = produtos.index('geladeira')
produto_escolhido = produtos[i]

# deletar valor
del produtos[1]

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

# ------Alterações incrementais
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

# ------Listas de listas - matrizes
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

# BREAK - Pausa o laço
# CONTINUE - Ignora a execução em determinada condição
# QUOCIENTE - dado por //
# RESTO - dado por %
for i in range(3,45,3):
    if i//3 == 8:
        break
    elif i % 2 == 0:
        continue
    else:
        print(f'{i} é impar')

# Condição de limite inferior e superior
nota = float(input('Informe uma nota entre 0 e 10: '))
while not (0 <= nota <= 10):
    print('Nota inválida')
    nota = float(input('Informe uma nota entre 0 e 10: '))

# ------TUPLAS
vendas = ('Lucas', '01/01/2024', '01/01/2000', 2000, 'Auxiliar')
# Recomendado utilizar try except, pois a quantidade de variáveis deve ser a mesma que a quantidade de valores. 
nome, data_contratacao, data_nascimento, salario, cargo = vendas

# enumerate, passando o índice e valor
# primeira variável representa o índice e a segunda representa o valor
# Ao percorrer uma lista desta forma, é retornada uma tupla.
for i, venda in enumerate(vendas):
        print('{} vendeu {} unidades'.format(funcionarios[i], venda))


# ------DICIONÁRIOS - Similar ao JSon

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}
# Obtendo e validando dados:
# Valida se a chave copo existe em tecnologia
if 'copo' in vendas_tecnologia:
    print(vendas_tecnologia['copo'])
else:
    print('copo não está na lista de produtos de tecnologia')

# Verifica se é encontrado algum valor com o dado
if vendas_tecnologia.get('copo') == None:
    print('Copo não está dentro da lista de produtos de tecnologia')
else:
    print(vendas_tecnologia.get('copo'))

# clear() -> Deleta todos os elementos do Dicionário (semelhante ao que aprendemos em listas)
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_mes.clear()
# copy() -> Cria uma cópia do dicionário (semelhante ao que aprendemos em listas)
vendas2_mes = vendas_mes.copy()
print(vendas2_mes)
# fromkeys(chaves, valor_padrao) -> Cria um dicionário com as chaves e o mesmo valor padrão para todas as chaves
chaves = ('jan', 'fev', 'mar')
vendas = 100
vendas_mes = dict.fromkeys(chaves, vendas)
# get(chave) -> 	Retorna o valor especificado pela chave (Semelhante a fazer dictionario[chave]
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(vendas_mes.get('mar'))
# items() -> Retorna uma lista em que cada item é uma tupla com (chave, valor)
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(list(vendas_mes.items()))
# keys() -> Retorna uma lista com todas as chaves do dicionário
print(list(vendas_mes.keys()))
# pop(chave) -> Retira o item do dicionário e retorna o valor dele para ser usado
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.pop('fev') #retira o fevereiro do dicionário ao mesmo tempo que armazena o valor dele na variável
print(vendas_mes)
print(vendas_fev)
# popitem() -> Retira o último item adicionado ao dicionário
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
#retira o último item adicionado no dicionário ao mesmo tempo que armazena o item(chave, valor) dele na variável
vendas_ult = vendas_mes.popitem() 
print(vendas_mes)
print(vendas_ult)
# Update - caso seja passado um dicionário fixo, modifica o dicionário
# caso seja passado uma variável que contenha um dicionário, 
# update(dicionario) -> Adiciona o dicionário passado como parâmetro ao dicionário original - adiciona ao final
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_2tri = {'abr': 400, 'mai': 600, 'jun': 500}
vendas_mes.update(vendas_2tri)
print(vendas_mes)
# update passando  atualiza o dicionário.
lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_1tri.update({'janeiro': 100000, 'fevereiro': 120000, 'março': 90000, 'abril': 88000})
print(lucro_1tri)
# setdefault(chave, valor) -> Retorna o valor da chave passada, mas caso a chave não exista, cria no dicionário o item com a chave e valor passados.
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.setdefault('fev', 500)
print(vendas_fev)
# omo fevereiro existe na lista, ele procura pelo valor de fevereiro e ignora o 500 passado
# agora quando não existe na lista:
vendas_abr = vendas_mes.setdefault('abr', 600)
# Agora além de vendas_abr retornar o 600 como valor, ele adicionou um item no dicionario
print(vendas_abr)
print(vendas_mes)
# values() -> Retorna uma lista com todos os valores do dicionários
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(list(vendas_mes.values()))
# Alterando (Caso já exista), ou adicionando algum valor:
lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_1tri['abril'] = 88000
# del - CUIDADO AO UTILIZAR - pode deletar o dicionário competo
# Exclui o valor armazenado em [0]
del lucro_1tri[0]
# Exclui todo o dicionário
del lucro_1tri


