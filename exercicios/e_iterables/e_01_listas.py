"""
Exercícios

1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

"""
2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""
# RESPOSTA:

vendas_ano = vendas_1sem + vendas_2sem
vendas_melhor_mes = max(vendas_ano)
vendas_pior_mes = min(vendas_ano)
melhor_mes = meses[vendas_ano.index(vendas_melhor_mes)]

print(f'O melhor mês do ano foi "{melhor_mes}", com R$ {vendas_melhor_mes:.2f} em vendas'.replace('.',',') + \
        '.\n' + f'O total de vendas do pior mês foi R$ {vendas_pior_mes:.2f}'.replace(".",","))

faturamento = sum(vendas_ano)
perc_melhor_mes =  vendas_melhor_mes/faturamento*100
print(f'O faturamento do melhor mês representa {perc_melhor_mes:.2f}% do faturamento total, \
que foi de R${faturamento:.2f}'.replace('.',','))


"""
3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
"""

top3 = []
var1 = vendas_ano.pop(vendas_ano.index(max(vendas_ano)))
top3.append(var1)
var1 = vendas_ano.pop(vendas_ano.index(max(vendas_ano)))
top3.append(var1)
var1 = vendas_ano.pop(vendas_ano.index(max(vendas_ano)))
top3.append(var1)

string_top3 = ', '.join(map(str, top3))
print(f'Os 3 maiores valores de venda são, respectivamente: {string_top3}')


"""
## 4. Mudança de Carga Tributária

- Reformas e mudanças de cargas tributárias são bem comuns no Brasil.

Digamos que você trabalhe em uma empresa de ecommerce

No Brasil, o imposto sobre livros é zerado. De um ano para o outro, o governo criou um novo imposto que incide em 10% sobre o valor dos livros e
agora você precisa alterar o registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.

Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar de custo para a empresa)

Obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve vamos aprender um for que vai adaptar esse cenário para qualquer quantidade de livros na sua lista.

Obs2: Seu código deve funcionar mesmo que não haja livros na lista de produtos da empresa
"""

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
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

taxa_imposto = 0.1
impacto_total = 0
for i in range(len(produtos)):
    nome = produtos[i].lower()
    vendas, preco = produtos_ecommerce[i]

    if "livro" in nome:
        imposto = preco * taxa_imposto
        produtos_ecommerce[i][1] += imposto
        impacto_total += vendas * imposto

        
print("Tabela atualizada de produtos:")
for i in range(len(produtos)):
    nome = produtos[i]
    vendas, preco = produtos_ecommerce[i]
    print(f'{nome.capitalize()}: {vendas} vendas, Preço: R$ {preco:.2f}'.replace(".", ","))

print(f"\nImpacto financeiro total do imposto: R$ {impacto_total:.2f}".replace(".", ","))

# EXERCÍCIOS EXTRA
# Exercício 1
# Crie um sistema de cadastro de produtos em uma lista de produtos
# Seu sistema deve:
# - Pegar o usuário qual produto vai ser cadastrado por meio de um input
# - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
# - Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

novo_produto = input("Digite o produto para cadastrar:").lower()

if novo_produto in produtos:
    print("Produto já existente, tente novamente")
else:
    produtos.append(novo_produto)
    print(f"Produto {novo_produto} cadastrado com sucesso")
    print(produtos)

# Exercício 2
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente

produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]
produto_procurado = input("Digite o produto:")
produto_procurado = produto_procurado.lower()
if produto_procurado in produtos:
    indice = produtos.index(produto_procurado)
    preco = precos[indice]
    print(f"Produto: {produto_procurado}, Preço: {preco}")
else:
    print("Produto não encontrado, tente novamente")

# Exercício 3
# Crie um sistema de consulta de bônus dos funcionários
# Seu sistema deve:
# - Pegar o valor de vendas do funcinoário por meio de um input
# - Calcular o bônus do funcionário de acordo com a seguinte regra:
#       - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
#       - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
#       - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
# - Printar no final o valor do bônus do funcionário

vendas = float(input("Digite as unidades vendidas (apenas números):"))
if vendas > 5000:
    bonus = vendas * 2 + 1000
elif vendas > 1000:
    bonus = vendas * 2
else:
    bonus = 0
print(f"Bônus {bonus}")


# Exercício 4
# Crie um programa que consiga descobrir qual dos vendedores vendeu mais
# As vendas dos vendedores são listas com a quantidade vendida por cada vendedor

vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],    
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]

vendas_vendedor1 = sum(vendas[0])
vendas_vendedor2 = sum(vendas[1])

if vendas_vendedor1 > vendas_vendedor2:
   print("Vendedor 1 vendeu mais")
else:
   print("Vendedor 2 vendeu mais")

"""
Exercício 5

vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]
a Quanto João vendeu de IPad?
b Quanto Diego vendeu de IPhone
c Qual o total de vendas de IPhone?
d E se Lira na verdade fez apenas 50 vendas de IPhone, como eu modifico na minha lista o valor de vendas dele?
e E se agora eu tenho um novo produto 'mac', como eu adiciono as vendas em cada um dos vendedores?

vendas_mac = [10,15,6,70]

"""
# RESPOSTA:
vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]
# a
vendas_ipad_joao = vendas[1][0]
print(vendas_ipad_joao)
# b
vendas_iphone_diego = vendas[2][1]
print(vendas_iphone_diego)
# c
vendas_iphone = 0
for i in range(len(vendas)):
    vendas_iphone += vendas[i][1]
print(vendas_iphone)
# d
vendas[0][1] = 50
# e
produtos.append('mac')
vendas_mac = [10,15,6,70]
for i in range(len(vendas)):
    vendas[i].append(vendas_mac[i])

print(vendas)