"""
Exercícios do Módulo 1 - Operações, Variáveis e Input

PARTE 1 - Operações e Variáveis
Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
Obs: faça tudo usando variáveis.

Valores do último ano:

Quantidade de Vendas de Coca = 1500
Quantidade de Vendas de Pepsi = 200
Preço Unitário da Coca = 1,50
Preço Unitário da Pepsi = 1,50
Custo da Loja: 2.500,00

1. Qual foi o faturamento de Pepsi da Loja?
2. Qual foi o faturamento de Coca da Loja?
3. Qual foi o Lucro da loja?
4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual

--------------------------
PARTE 2 - Inputs e Strings
A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
Ex: 
Coca -> Código: BEB1300543<br>
Pepsi -> Código: BEB1300545<br>
Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
Vodka Smirnoff -> Código: BAC17675002<br>

Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder
True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.

"""
qtd_vendas_coca = 1500
qtd_vendas_pepsi = 200
preco_coca = 1.5
preco_pepsi = 1.5
Custo_loja = 2500

faturamento_pepsi = qtd_vendas_pepsi * preco_pepsi
faturamento_coca = qtd_vendas_coca * preco_coca
faturamento = faturamento_coca + faturamento_pepsi 
lucro = faturamento - faturamento_coca
margem = lucro/faturamento
print(f"Faturamento Pepsi: {faturamento_pepsi:,.2f}")
print(f"Faturamento Coca: {faturamento_coca:,.2f}")
print(f"Lucro: {lucro:,.2f}")
print(f"Margem: {margem:,.2%}")


alcolica = input('Digite o código: ')
print('Código é de bebida alcóolica? ' + str('BAC' in alcolica.upper()))

