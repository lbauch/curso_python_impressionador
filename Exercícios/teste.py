vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_2tri = {'abr': 400, 'mai': 600, 'jun': 500}
vendas_mes.update(vendas_2tri)
print(vendas_mes)
# update passando  atualiza o dicionário.
lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_1tri.update({'janeiro': 100000, 'fevereiro': 120000, 'março': 90000, 'abril': 88000})
print(lucro_1tri)