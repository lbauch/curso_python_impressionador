# Para mais informações, w3schools é muito boa para Python

# importante:
# \n - pula linha
# \t - tab
# \r - vai para o início da mesma linha e sobrescreve (somente sobrescreve a mesma qtd de dígitos)
import time
print('teste 10', end='\r')
time.sleep(1)
print('teste 2')
time.sleep(1)
print('teste 10', end=' \r')
time.sleep(1)
print('teste 2', end=' \r')
time.sleep(1)

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

# sep - define o separador ao utilizar a função
# sep deve ser o último parâmetro
print(1, 2, 3, sep = ';')

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
# Try Except else finally
# WHILE
while True:
    try:
        total_estoque = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    else:
# Executa o else somente se não resultar em erro.
        print('número informado é válido')
# Executa o finally caso ocorra ou não o erro.
    finally:
        print('fim do while')



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

# Funções importantes de strings
# - capitalize() -> Coloca a 1ª letra Maiúscula
# - casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)
# - count()	-> Quantidade de vezes que um valor aparece na string
# - endswith() -> Verifica se o texto termina com um valor específico e dá como resposta True ou False
# - find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado
# - format() -> Formata uma string de acordo com os valores passados. Já usamos bastante ao longo do programa.
# - isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função.
# - isalpha() -> Verifica se um texto é todo feito de letras.
# - isnumeric()	-> Verifica se um texto é todo feito por números.
# - replace() -> Substitui um texto por um outro texto em uma string.
# - split()	-> Separa uma string de acordo com um delimitador em vários textos diferentes.
# - splitlines() -> separa um texto em vários textos de acordo com as quebras de linha do texto
# - startswith() -> Verifica se a string começa com determinado texto
# - strip()	-> Retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no início e no final
# - title() -> Coloca a 1ª letra de cada palavra em maiúscula
# - upper()	-> Coloca o texto todo em letra maiúscula
# - strip() -> Remove espaços no início e no final.

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
# Cuidado ao utilizar, pois pode excluir toda a variável
del produtos[1]

# Organizar lista:
# Por padrão, organiza em ordem crescente. - reverse = false
# Para organizar em formato decrescente, necessário colocar o parâmetro reverse = true
produtos.sort()
print(produtos)
produtos.sort(reverse = True)
print(produtos)

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
for mes, qtd in vendas_mes.items():
    print('{}: {} unidades'.format(produto, qtd))
print(list(vendas_mes.items()))

# Percorrendo o dicionário
bonus = []
vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000
for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] * 0.1)
    else:
        bonus.append(0)

# keys() -> Retorna uma lista com todas as chaves do dicionário
# Ao adicionar, remover ou alterar itens do dicionário, faz as modificações na variável criada também.
# Neste caso, a variável criada é listas_dicionario, que será alterada caso o dicionário seja modificado
# Ao imprimir o dict.keys(), imprime em formato de dicionário.
# Ao utilizar o list(dict.keys()), imprime como lista
listas_dicionario = vendas_mes.keys()
vendas_mes['abr'] = 160
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
# update passando dicionário completo - atualiza o dicionário.
lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_1tri.update({'janeiro': 100000, 'fevereiro': 120000, 'março': 90000, 'abril': 88000})
print(lucro_1tri)
# setdefault(chave, valor) -> Retorna o valor da chave passada, mas caso a chave não exista, cria no dicionário o item com a chave e valor passados.
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.setdefault('fev', 500)

print(vendas_fev)
# Como fevereiro existe na lista, ele procura pelo valor de fevereiro e ignora o 500 passado
# Agora quando não existe na lista:
vendas_abr = vendas_mes.setdefault('abr', 600)
# Agora além de vendas_abr retornar o 600 como valor, ele adicionou um item no dicionario
print(vendas_abr)
print(vendas_mes)
# values() -> Retorna uma lista com todos os valores do dicionários
# Ao adicionar, remover ou alterar itens do dicionário, faz as modificações na variável criada também.
# Neste caso, a variável criada é listas_dicionario, que será alterada caso o dicionário seja modificado
# Ao imprimir o dict.values(), imprime em formato de dicionário.
# Ao utilizar o list(dict.values()), imprime como lista
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
listas_dicionario = vendas_mes.values()
print(listas_dicionario)
vendas_mes['abr'] = 160
print(list(vendas_mes.values()))
# Alterando (Caso já exista), ou adicionando algum valor:
lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_1tri['abril'] = 88000
# del - CUIDADO AO UTILIZAR - pode deletar o dicionário competo
# Exclui o valor armazenado em [0]
del lucro_1tri[0]
# Exclui todo o dicionário
del lucro_1tri

# Percorrendo e obtendo valores de um dicionário
vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
total_notebooks = 0
for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]
        
print(total_notebooks)

# Interpretando dados em um dicionário - JSon
video = {'uri': '/videos/465407533', 'name': '15 Atalhos no Excel para Ficar Mais Produtivo', 'download': [{'quality': 'source', 'type': 'source', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064518513?s=465407533_1602043255_5f2f93dd00b66eba66d481f913383b4f&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivosource.mp4', 'created_time': '2020-10-06T14:26:17+00:00', 'fps': 30, 'size': 402678442, 'md5': 'af09508ceceed4994554f04e8b931e22', 'public_name': 'Original', 'size_short': '384.02MB'}, {'quality': 'hd', 'type': 'video/mp4', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523157?s=465407533_1602043255_ab7b8353c59b5048032396ec5d95a276&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo175.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 173556205, 'md5': '3c05e1e69bd6b13eb1464451033907d2', 'public_name': 'HD 1080p', 'size_short': '165.52MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 960, 'height': 540, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523153?s=465407533_1602043255_f5ac38009ec5c0a13b30600c631446a3&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo165.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 89881848, 'md5': '4a5c5c96cdf18202ed20ca534fd88007', 'public_name': 'SD 540p', 'size_short': '85.72MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 426, 'height': 240, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522788?s=465407533_1602043255_16c69872e2c4e92cc949d0b772242959&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo139.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 27401450, 'md5': '91cc0229087ec94bf67f64b01ad8768d', 'public_name': 'SD 240p', 'size_short': '26.13MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 640, 'height': 360, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522787?s=465407533_1602043255_310b087e2fc8c5e1154ce7a33d10d60e&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo164.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 48627155, 'md5': '548640bf79ce1552a3401726bb0e4224', 'public_name': 'SD 360p', 'size_short': '46.37MB'}]}
print(video)
for item in video:
    print(item)

# Encontra a chave download,
# Como download é um array, pega o primeiro item
# Pega o valor da chave como nome link
print(video['download'][0]['link'])

"""
- Dicionário com valores padrões:

dicionario = dict.fromkeys(lista_chaves, valor_padrao)

- Dicionário a partir de listas de tuplas:

dicionario = dict(lista_tuplas)

- Dicionário a partir de 2 listas:

Passo 1: Transformar listas em lista de tuplas com o método zip
Passo 2: Transformar em dicionario

lista_tuplas = zip(lista1, lista2)
dicionario = dict(lista_tuplas)
"""
produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]
# zip une as duas listas com os valores
# transforma em uma lista de tuplas
lista_tuplas = zip(produtos, vendas)
# Caso seja impressa a lista criada, é retornado um endereço de memória.
print(lista_tuplas)
# Necessário criar um dicionário através do dict
# Para uma lista, usar list
# dict cria um dicionário com a lista de tuplas
# FUNÇÃO DICT
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)


#  ------ITERABLES

# Tuplas, dicionários, strings e listas são iterables.
# Conjunto de dados que pode ser percorrido

# set - Parecido com o dicionário, porém, contém somente valores, não possui chaves
# Não possui ordem fixa
# Não possui valores duplicados. Pode ser uma forma de remover duplicatas de listas


#  ------FUNCTIONS

# Obs Importante: a função deve estar SEMPRE antes de ser usada.

# Normalmente, nos nossos códigos, fazemos as definições de todas as funções antes e depois construimos o resto do código.
# É comum dar '2 enters' após a definição da função para deixar o código mais organizado
def func1 (par_1, par_2, par_n):
    return par_1 + par_2 + par_n


def categoria_produto(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False


produtos = ['CAR46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510',\
            'TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623',\
            'BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495',\
            'TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311',\
            'TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947',\
            'TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262',\
            'BSA96915','CAR53454','BEB75073']

# Ao utilizar, temos 2 formas de atribuição:
for produto in produtos:
# Forma 1: Atribuindo a ordem específica de atribuição, definindo os nomes corretamente
    #if categoria_produto(bebida = produto, cod_categoria = 'BEB'):
    if categoria_produto(produto, cod_categoria = 'BEB'):
        print('Enviar {} para setor de bebidas alcóolicas'.format(produto))
# Forma 2: Passando os parâmetros que serão atribuídos na ordem de entrada
    elif categoria_produto(produto, 'BSA'):
        print('Enviar {} para setor de bebidas não alcóolicas'.format(produto))
# Ao passar um parâmetro com palavra chaves, todos os parâmetros seguintes à direita precisam estar também.

# Definir valores padrão para um parâmetro:
# atribui 'm' como valor padrão do parâmetro padrão
def padronizar_codigos(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos


# Functions retornando mais de um valor
# Resultado do return é uma tupla
precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37,2.4,1.72,2,1.69,1.63,2.01,2.25,1.61,1.02,1.19,1.86,2.15,2.03,1.61,1.52,1.56,1.69,1.47,1.09,2.47,1.62,2.15,1.81,2.49,2.08,1.02,1.68,1.53,1.2,1.29,1.88,1.92,2.14,1.95,2.48,2.44,1.41,1.98,1.89,1.69,1.95,1.42,1.57,2.32,1.23,1.43,1.35,1.49,2.39,2.37,1.3,2.25,1.5,1.35,2.06,1.05,1.7,2.29,2.44,2.09,1.81,2.04,2.45,1.42,2.09,2.19,2.09,1,2.23,1.39,2,1.29,1.55,1.67,2.06,1.89,2.07,2.39,1.93,1.51,1.73,1.66,1.18,1.13,1.69,2.48,1.26,1.75, 1.51, 1.73]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147,222,165,184,175,147,217,214,171,86,111,180,211,210,168,156,154,179,163,99,246,162,205,195,263,198,121,149,140,122,119,197,210,218,202,258,256,135,203,173,152,197,145,154,252,141,141,151,133,232,229,134,215,155,138,186,120,152,213,256,219,200,210,238,140,224,233,222,120,233,151,185,111,149,186,194,194,222,223,185,157,154,164,129,128,169,240,136,191, 157, 154]


def separar_listas(precos, tamanhos, fator=0.1):
        if len(precos) == len(tamanhos):
            #executar o codigo
            i = int((1 - fator) * len(precos))
            precos_imoveis_treino = precos[:i]
            precos_imoveis_teste = precos[i:]
            tamanho_imoveis_teste = tamanhos[i:]
            tamanho_imoveis_treino = tamanhos[:i]
            return precos_imoveis_treino, precos_imoveis_teste, tamanho_imoveis_treino, tamanho_imoveis_teste
        else:
            print('As listas de precos e tamanhos dos imoveis não têm a mesma quantidade de itens')
            return
        
# raise - importante para functions
def minha_soma(num1, num2, num3, num4):
    # Verificar os tipos dos parâmetros
    if not isinstance(num1, int):
        raise TypeError("num1 deve ser um inteiro!")
    if not isinstance(num2, str):
        raise TypeError("num2 deve ser uma string!")
    if not isinstance(num3, bool):
        raise TypeError("num3 deve ser um booleano!")
    if not isinstance(num4, float):
        raise TypeError("num4 deve ser um número de ponto flutuante!")

    # Realizar algum processamento (exemplo de soma, se desejado)
    return f"Soma de valores: {num1} + {num4} = {num1 + num4}"

# Exemplos de uso
try:
    resultado = minha_soma(1, "exemplo", True, 3.5)  # Correto
    print(resultado)  # Saída: Soma de valores: 1 + 3.5 = 4.5

    resultado = minha_soma(1, "exemplo", True, "3.5")  # Incorreto
except TypeError as e:
    print(e)

# IMPORTANTE
# Funções com quantidade de parâmetros indefinida
# Após o asterisco, não se pode mais usar parâmetros.

# ** define o valor recebido e a chave - retorna como um dicionário único
def preco_final(preco, **adicionais):
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra'] 
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

print(preco_final(1000, desconto=0.1, garantia_extra = 100, imposto=0.3))

# Outra forma:
def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
# Atribui quantos parâmetros forem necessários.
print(minha_soma(10, 13, 1, 10, 90, 0, 9, 8))

# Ordem dos Argumentos

### Estrutura:

# - Sempre os positional arguments vêm antes e depois os keywords arguments.
# - Sempre os argumentos individuais vêm antes e depois os "múltiplos"

# def minha_funcao(arg1, arg2, arg3, arg4, *args, k = kwarg1, k2 = kwarg2, k3 = kwarg3, **kwargs):
#     ...

def minha_soma(arg1, arg2, *args1, arg3, arg4, **args2):
    soma = 0
    soma += arg1 + arg2
    print(soma)
    for arg in args1:
        soma += arg
    print(soma)
    soma += arg3 + arg4
    print(soma)
    for key,value in args2.items():
        print(value)
# Atribui quantos parâmetros forem necessários.
print(minha_soma(10, 5, 1, 10, arg3 = 90, arg4 =  3, arg5 = 9, arg6 = 8))


# ------LIST COMPREHENSION
preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

# Forma aprendida até agora
impostos = []
for item in preco_produtos:
    impostos.append(item * 0.3)
print(impostos)

# Utilizando list comprehension
impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)

# Utilizando functions dentro do list_comprehension
def calcular_imposto(preco, imposto):
    return preco * imposto

impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]
print(impostos)

# Ordenando duas listas relacionadas com zip
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

lista_aux = list(zip(vendas_produtos, produtos))
lista_aux.sort(reverse=True)
produtos = [produto for vendas, produto in lista_aux]
print(produtos)

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]
vendas2019 = [(produto, vendas_2019) for produto, vendas_2019, vendas2020 in vendas_produtos]
print(vendas2019)

# List comprehension com condição
# Para filtro
meta = 1000
vendas = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']
produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)

# Para alterar o resultado final
vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000

bonus = []

for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] * 0.1)
    else:
        bonus.append(0)
print(bonus)

# Ao utilizar o if else antes do for, 
bonus = [vendedores_dic[item] * 0.1 if vendedores_dic[item] > meta else 0 for item in vendedores_dic]
print(bonus)

# List comprehension para outras funções em iterable
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']

total_top5 = sum(vendas[i] for i, produto in enumerate(produtos) if produto in top5)
print(total_top5)
print('Top 5 representou {:0.1%} das vendas'.format(total_top5/sum(vendas)))

# ----------- MÓDULO TIME
import time
# Aguarda 5 segundos para continuar
time.sleep(5)

# Marco Zero: EPOCH (01 de janeiro de 1970 às 00:00:00)
# time() retorna quantos segundos se passaram desde a EPOCH
segundos_hoje = time.time()
print(segundos_hoje)

# ctime() retorna a data em string
data_hoje = time.ctime()
print(data_hoje)

# gmtime retorna no padrão utc 0 - Greenwich
# localtime retorna o horário do computador
hora_geral = time.gmtime()
hora_local = time.localtime()
print(hora_geral)
print(hora_local)

# pegar o dia, mês e ano
dia = hora_local.tm_mday
mes = hora_local.tm_mon
ano = hora_local.tm_year
dia_da_semana = hora_local.tm_wday

print("Data: {}/{}/{}".format(dia, mes, ano))
print(f"Data: {dia}/{mes}/{ano}")

# IMPORTANTE:LOCALE
# No início de cada código, é importante colocar a instrução:
# Necessário configurar somente uma vez no código
import locale
# O código abaixo é usado para padronizar tudo para pt_BR e UTF-8.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Padrozinar utilização de datas em python:
# Utiliza-se a função strptime(string_tempo, formato)
string_tempo = "30 Junho, 2023"
formato = "%d %B, %Y"
tempo_em_struct = time.strptime(string_tempo, formato)
print(f"Tempo em struct: {tempo_em_struct}")

# time.maketime()
# Utilizada para fazer comparações - lib time exige que os tempos sejam passados para segundos
tempo_em_struct = time.localtime()
tempo_em_segundos = time.mktime(tempo_em_struct)
print(f"Tempo em segundos: {tempo_em_segundos}")
print(f"Tempo em segundos: {time.time()}")

# maketime() utilizando uma tupla:
# Formato da saída de time.struct:
# time.struct_time(tm_year=2023, tm_mon=6, tm_mday=29, tm_hour=10, tm_min=20, tm_sec=0, tm_wday=3, tm_yday=180, tm_isdst=0)
tempo_ano_novo = time.mktime((2023, 1, 1, 0, 0, 0, 0, 0, 0))

# Contagem regressiva:
import time
# Necessário utilizar o ' \r' com espaço na frente, pois sobrescreve a mesma quantidade de dígitos
for i in range(10, 0, -1):
    print(i, end=" \r")
    time.sleep(1)
print("O evento começou!") 