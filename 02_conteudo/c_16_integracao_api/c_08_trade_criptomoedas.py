# IMPORTANTE
# NÃO CHAMAR A PASTA OU O ARQUIVO DE binance, para não conflitar com o nome real da lib - evitar usar o nome binance
# !pip install python-binance
# Caso não reconheça a instalação talvez seja necessário alterar o nome da lib e noms imports alterar também.

# Para mais informações, acessar a doc da api

# Para obter api_key, api_secret - ir no binance > gerenciamento de api e obter os dados
from binance.client import Client
from secrets import api_secret, api_key

client = Client(api_key, api_secret)

# pegar informações da nossa conta
info = client.get_account()
for item in info:
    print(item)

# ver os saldos dos ativos que temos na conta
lista_ativos = info["balances"]
# print(lista_ativos)
# ativos que temos algum saldo
for ativo in lista_ativos:
    if float(ativo["free"]) > 0:
        print(ativo)

# criar uma ordem dentro da binance
from binance.enums import *
order = client.create_order(
    # Par de símbolos para representar quais itens se quer trocar
    # Para verificar os pares, ir na conta da binance em trade > clássico, pode-se encontrar todos os pares possíveis de moeda
    # A ordem importa - define qual se quer vender e qual comprar
    symbol='BNBBRL',
    # SIDE_BUY ou SIDE_SELL. Buy - compra a primeira moeda usando a segunda. Sell - vende a primeira para comprar a segunda
    side=SIDE_SELL,
    # Market - valor da tela de negociação
    type=ORDER_TYPE_MARKET,
    # A quantidade refere-se ao primeiro item do par
    quantity=0.01,
    )
print(order)

# visualizar as ordens executadas
print(client.get_all_orders(symbol='BNBBRL'))
print(client.get_my_trades(symbol='BNBBRL'))

# te mostrar as referências de cada par de moedas
print(client.get_symbol_info('BNBBRL')) # Entre outras infos, mostra a qutd mínima que pode ser negociada

# pegar as cotações em tempo real
transacoes = client.get_recent_trades(symbol="BNBBRL", limit=1)
print(transacoes)