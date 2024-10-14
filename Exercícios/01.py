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
qtdVendas_Coca = 1500
qtdVendas_Pepsi = 200
preco_Coca = 1.5
preco_Pepsi = 1.5
CustoLoja = 2500

fatPepsi = qtdVendas_Pepsi * preco_Pepsi
fatCoca = qtdVendas_Coca * preco_Coca
faturamento = fatCoca + fatPepsi 
lucro = faturamento - CustoLoja
margem = lucro/faturamento
print(f"Faturamento Pepsi: {fatPepsi:,.2f}")
print(f"Faturamento Coca: {fatCoca:,.2f}")
print(f"Lucro: {lucro:,.2f}")
print(f"Margem: {margem:,.2%}")


alcolica = input('Digite o código: ')
print('Código é de bebida alcóolica? ' + str('BAC' in alcolica.upper()))
