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